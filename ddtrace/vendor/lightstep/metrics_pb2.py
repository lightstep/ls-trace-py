# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metrics.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ddtrace.vendor.lightstep.collector_pb2 as collector__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="metrics.proto",
    package="lightstep.metrics",
    syntax="proto3",
    serialized_options=_b("\n\031com.lightstep.tracer.grpcP\001Z\tmetricspb\242\002\004LSPB"),
    serialized_pb=_b(
        '\n\rmetrics.proto\x12\x11lightstep.metrics\x1a\x0f\x63ollector.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8f\x02\n\x0bMetricPoint\x12+\n\x04kind\x18\x01 \x01(\x0e\x32\x1d.lightstep.metrics.MetricKind\x12\x13\n\x0bmetric_name\x18\x02 \x01(\t\x12)\n\x05start\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x64uration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12-\n\x06labels\x18\x05 \x03(\x0b\x32\x1d.lightstep.collector.KeyValue\x12\x16\n\x0cuint64_value\x18\x06 \x01(\x04H\x00\x12\x16\n\x0c\x64ouble_value\x18\x07 \x01(\x01H\x00\x42\x07\n\x05value"\x89\x01\n\rIngestRequest\x12\x17\n\x0fidempotency_key\x18\x01 \x01(\t\x12/\n\x08reporter\x18\x02 \x01(\x0b\x32\x1d.lightstep.collector.Reporter\x12.\n\x06points\x18\x03 \x03(\x0b\x32\x1e.lightstep.metrics.MetricPoint"\x10\n\x0eIngestResponse*=\n\nMetricKind\x12\x17\n\x13INVALID_METRIC_KIND\x10\x00\x12\x0b\n\x07\x43OUNTER\x10\x01\x12\t\n\x05GAUGE\x10\x02\x42/\n\x19\x63om.lightstep.tracer.grpcP\x01Z\tmetricspb\xa2\x02\x04LSPBb\x06proto3'
    ),
    dependencies=[
        collector__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)

_METRICKIND = _descriptor.EnumDescriptor(
    name="MetricKind",
    full_name="lightstep.metrics.MetricKind",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="INVALID_METRIC_KIND", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(name="COUNTER", index=1, number=1, serialized_options=None, type=None),
        _descriptor.EnumValueDescriptor(name="GAUGE", index=2, number=2, serialized_options=None, type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=550,
    serialized_end=611,
)
_sym_db.RegisterEnumDescriptor(_METRICKIND)

MetricKind = enum_type_wrapper.EnumTypeWrapper(_METRICKIND)
INVALID_METRIC_KIND = 0
COUNTER = 1
GAUGE = 2


_METRICPOINT = _descriptor.Descriptor(
    name="MetricPoint",
    full_name="lightstep.metrics.MetricPoint",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="kind",
            full_name="lightstep.metrics.MetricPoint.kind",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="metric_name",
            full_name="lightstep.metrics.MetricPoint.metric_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="start",
            full_name="lightstep.metrics.MetricPoint.start",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="duration",
            full_name="lightstep.metrics.MetricPoint.duration",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="labels",
            full_name="lightstep.metrics.MetricPoint.labels",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="uint64_value",
            full_name="lightstep.metrics.MetricPoint.uint64_value",
            index=5,
            number=6,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="double_value",
            full_name="lightstep.metrics.MetricPoint.double_value",
            index=6,
            number=7,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="value", full_name="lightstep.metrics.MetricPoint.value", index=0, containing_type=None, fields=[]
        ),
    ],
    serialized_start=119,
    serialized_end=390,
)


_INGESTREQUEST = _descriptor.Descriptor(
    name="IngestRequest",
    full_name="lightstep.metrics.IngestRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="idempotency_key",
            full_name="lightstep.metrics.IngestRequest.idempotency_key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="reporter",
            full_name="lightstep.metrics.IngestRequest.reporter",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="points",
            full_name="lightstep.metrics.IngestRequest.points",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=393,
    serialized_end=530,
)


_INGESTRESPONSE = _descriptor.Descriptor(
    name="IngestResponse",
    full_name="lightstep.metrics.IngestResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=532,
    serialized_end=548,
)

_METRICPOINT.fields_by_name["kind"].enum_type = _METRICKIND
_METRICPOINT.fields_by_name["start"].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_METRICPOINT.fields_by_name["duration"].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_METRICPOINT.fields_by_name["labels"].message_type = collector__pb2._KEYVALUE
_METRICPOINT.oneofs_by_name["value"].fields.append(_METRICPOINT.fields_by_name["uint64_value"])
_METRICPOINT.fields_by_name["uint64_value"].containing_oneof = _METRICPOINT.oneofs_by_name["value"]
_METRICPOINT.oneofs_by_name["value"].fields.append(_METRICPOINT.fields_by_name["double_value"])
_METRICPOINT.fields_by_name["double_value"].containing_oneof = _METRICPOINT.oneofs_by_name["value"]
_INGESTREQUEST.fields_by_name["reporter"].message_type = collector__pb2._REPORTER
_INGESTREQUEST.fields_by_name["points"].message_type = _METRICPOINT
DESCRIPTOR.message_types_by_name["MetricPoint"] = _METRICPOINT
DESCRIPTOR.message_types_by_name["IngestRequest"] = _INGESTREQUEST
DESCRIPTOR.message_types_by_name["IngestResponse"] = _INGESTRESPONSE
DESCRIPTOR.enum_types_by_name["MetricKind"] = _METRICKIND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetricPoint = _reflection.GeneratedProtocolMessageType(
    "MetricPoint",
    (_message.Message,),
    {
        "DESCRIPTOR": _METRICPOINT,
        "__module__": "metrics_pb2"
        # @@protoc_insertion_point(class_scope:lightstep.metrics.MetricPoint)
    },
)
_sym_db.RegisterMessage(MetricPoint)

IngestRequest = _reflection.GeneratedProtocolMessageType(
    "IngestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _INGESTREQUEST,
        "__module__": "metrics_pb2"
        # @@protoc_insertion_point(class_scope:lightstep.metrics.IngestRequest)
    },
)
_sym_db.RegisterMessage(IngestRequest)

IngestResponse = _reflection.GeneratedProtocolMessageType(
    "IngestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _INGESTRESPONSE,
        "__module__": "metrics_pb2"
        # @@protoc_insertion_point(class_scope:lightstep.metrics.IngestResponse)
    },
)
_sym_db.RegisterMessage(IngestResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
