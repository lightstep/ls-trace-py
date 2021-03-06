import copy
import os
import re
import sys

from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# ORDER MATTERS
# Import this after setuptools or it will fail
from Cython.Build import cythonize  # noqa: I100
import Cython.Distutils


HERE = os.path.dirname(os.path.abspath(__file__))


def load_module_from_project_file(mod_name, fname):
    """
    Helper used to load a module from a file in this project

    DEV: Loading this way will by-pass loading all parent modules
         e.g. importing `ddtrace.vendor.psutil.setup` will load `ddtrace/__init__.py`
         which has side effects like loading the tracer
    """
    fpath = os.path.join(HERE, fname)

    if sys.version_info >= (3, 5):
        import importlib.util

        spec = importlib.util.spec_from_file_location(mod_name, fpath)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    elif sys.version_info >= (3, 3):
        from importlib.machinery import SourceFileLoader

        return SourceFileLoader(mod_name, fpath).load_module()
    else:
        import imp

        return imp.load_source(mod_name, fpath)


HERE = os.path.dirname(os.path.abspath(__file__))


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    This method prevents to import packages at setup-time.
    """
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


class Tox(TestCommand):

    user_options = [("tox-args=", "a", "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex

        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


version = get_version("ddtrace")

long_description = """
# ls-trace-py

Datadog has generously announced the [donation][donation post] of their tracer libraries
to the [OpenTelemety][opentelemetry docs] project. Auto-instrumentation
is a core feature of these libraries, making it possible to create and
collect telemetry data without needing to change your code. LightStep
wants you to be able to use these libraries now! We've forked the Datadog
libraries into the LightStep repo as agents. You can install and use these agents to take advantage of
auto-instrumentation without waiting for OpenTelemetry. Each LightStep agent
is "pinned" to a Datadog release and is fully supported by LightStep's
Customer Success team.

Simply install the agent, configure it to communicate with LightStep
Satellites, run your app, and then any [frameworks][framework docs], [data stores][datastore docs],
and [libraries][libs] included in your app will send data to LightStep as distributed traces.

[donation post]: https://www.datadoghq.com/blog/opentelemetry-instrumentation/
[opentelemetry docs]: https://opentelemetry.io/
[framework docs]: https://docs.lightstep.com/docs/python-auto-instrumentation#section-frameworks
[datastore docs]: https://docs.lightstep.com/docs/python-auto-instrumentation#section-data-stores
[libs]: https://docs.lightstep.com/docs/python-auto-instrumentation#section-libraries
"""

# Base `setup()` kwargs without any C-extension registering
setup_kwargs = dict(
    name="ls-trace",
    version=version,
    description="Datadog tracing code",
    url="https://github.com/lightstep/ls-trace-py",
    author="LightStep",
    author_email="support@lightstep.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(exclude=["tests*"]),
    # enum34 is an enum backport for earlier versions of python
    # funcsigs backport required for vendored debtcollector
    # encoding using msgpack
    install_requires=[
        "backoff>=1.8.0",
        "enum34; python_version<'3.4'",
        "funcsigs>=1.0.0;python_version=='2.7'",
        "googleapis-common-protos>=1.51.0",
        "msgpack>=0.5.0",
        "protobuf>=3.11.3",
        "requests",
    ],
    extras_require={
        # users can include opentracing by having:
        # install_requires=['ddtrace[opentracing]', ...]
        "opentracing": ["opentracing>=2.0.0"],
        "profile": ["protobuf>=3", "intervaltree",],
    },
    # plugin tox
    tests_require=["tox", "flake8"],
    cmdclass={"test": Tox, "build_ext": Cython.Distutils.build_ext},
    entry_points={
        "console_scripts": [
            "ls-trace-run = ddtrace.commands.ddtrace_run:main",
            "pyddprofile = ddtrace.profile.__main__:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm", "cython"],
    ext_modules=cythonize(
        [
            Cython.Distutils.Extension(
                "ddtrace.profile.collector.stack",
                sources=["ddtrace/profile/collector/stack.pyx"],
                language="c",
                extra_compile_args=["-DPy_BUILD_CORE"],
            ),
            Cython.Distutils.Extension(
                "ddtrace.profile.collector._traceback",
                sources=["ddtrace/profile/collector/_traceback.pyx"],
                language="c",
            ),
            Cython.Distutils.Extension("ddtrace.profile._build", sources=["ddtrace/profile/_build.pyx"], language="c",),
        ],
        compile_time_env={
            "PY_MAJOR_VERSION": sys.version_info.major,
            "PY_MINOR_VERSION": sys.version_info.minor,
            "PY_MICRO_VERSION": sys.version_info.micro,
        },
    ),
)


if sys.platform == "win32":
    build_ext_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError, IOError, OSError)
else:
    build_ext_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError)


class BuildExtFailed(Exception):
    pass


# Attempt to build a C-extension, catch exceptions so failed building skips the extension
# DEV: This is basically what `distutils`'s' `Extension(optional=True)` does
class optional_build_ext(Cython.Distutils.build_ext):
    def run(self):
        try:
            Cython.Distutils.build_ext.run(self)
        except DistutilsPlatformError as e:
            extensions = [ext.name for ext in self.extensions]
            print("WARNING: Failed to build extensions %r, skipping: %s" % (extensions, e))

    def build_extension(self, ext):
        try:
            Cython.Distutils.build_ext.build_extension(self, ext)
        except build_ext_errors as e:
            print("WARNING: Failed to build extension %s, skipping: %s" % (ext.name, e))


def get_exts_for(name):
    try:
        mod = load_module_from_project_file(
            "ddtrace.vendor.{}.setup".format(name), "ddtrace/vendor/{}/setup.py".format(name)
        )
        return mod.get_extensions()
    except Exception as e:
        print("WARNING: Failed to load %s extensions, skipping: %s" % (name, e))
        return []


# Try to build with C extensions first, fallback to only pure-Python if building fails
try:
    all_exts = []
    for extname in ("wrapt", "psutil"):
        exts = get_exts_for(extname)
        if exts:
            all_exts.extend(exts)

    kwargs = copy.deepcopy(setup_kwargs)
    kwargs["ext_modules"] += all_exts
    # DEV: Make sure `cmdclass` exists
    kwargs.setdefault("cmdclass", dict())
    kwargs["cmdclass"]["build_ext"] = optional_build_ext
    setup(**kwargs)
except Exception as e:
    # Set `DDTRACE_BUILD_TRACE=TRUE` in CI to raise any build errors
    if os.environ.get("DDTRACE_BUILD_RAISE") == "TRUE":
        raise

    print("WARNING: Failed to install with ddtrace C-extensions, falling back to pure-Python only extensions: %s" % e)
    setup(**setup_kwargs)
