# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mixer/adapter/model/v1beta1/report.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mixer/adapter/model/v1beta1/report.proto',
  package='istio.mixer.adapter.model.v1beta1',
  syntax='proto3',
  serialized_options=_b('Z(istio.io/api/mixer/adapter/model/v1beta1\310\341\036\000\250\342\036\000\360\341\036\000'),
  serialized_pb=_b('\n(mixer/adapter/model/v1beta1/report.proto\x12!istio.mixer.adapter.model.v1beta1\x1a\x14gogoproto/gogo.proto\"\x0e\n\x0cReportResultB6Z(istio.io/api/mixer/adapter/model/v1beta1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00\xf0\xe1\x1e\x00\x62\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_REPORTRESULT = _descriptor.Descriptor(
  name='ReportResult',
  full_name='istio.mixer.adapter.model.v1beta1.ReportResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['ReportResult'] = _REPORTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReportResult = _reflection.GeneratedProtocolMessageType('ReportResult', (_message.Message,), dict(
  DESCRIPTOR = _REPORTRESULT,
  __module__ = 'mixer.adapter.model.v1beta1.report_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.adapter.model.v1beta1.ReportResult)
  ))
_sym_db.RegisterMessage(ReportResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
