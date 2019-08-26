# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/http/authn/v2alpha1/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from authentication.v1alpha1 import policy_pb2 as authentication_dot_v1alpha1_dot_policy__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/filter/http/authn/v2alpha1/config.proto',
  package='istio.envoy.config.filter.http.authn.v2alpha1',
  syntax='proto3',
  serialized_options=_b('Z4istio.io/api/envoy/config/filter/http/authn/v2alpha1'),
  serialized_pb=_b('\n4envoy/config/filter/http/authn/v2alpha1/config.proto\x12-istio.envoy.config.filter.http.authn.v2alpha1\x1a$authentication/v1alpha1/policy.proto\"\xae\x02\n\x0c\x46ilterConfig\x12\x35\n\x06policy\x18\x01 \x01(\x0b\x32%.istio.authentication.v1alpha1.Policy\x12\x80\x01\n\x1cjwt_output_payload_locations\x18\x02 \x03(\x0b\x32Z.istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig.JwtOutputPayloadLocationsEntry\x12\"\n\x1askip_validate_trust_domain\x18\x03 \x01(\x08\x1a@\n\x1eJwtOutputPayloadLocationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x36Z4istio.io/api/envoy/config/filter/http/authn/v2alpha1b\x06proto3')
  ,
  dependencies=[authentication_dot_v1alpha1_dot_policy__pb2.DESCRIPTOR,])




_FILTERCONFIG_JWTOUTPUTPAYLOADLOCATIONSENTRY = _descriptor.Descriptor(
  name='JwtOutputPayloadLocationsEntry',
  full_name='istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig.JwtOutputPayloadLocationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig.JwtOutputPayloadLocationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig.JwtOutputPayloadLocationsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=444,
)

_FILTERCONFIG = _descriptor.Descriptor(
  name='FilterConfig',
  full_name='istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy', full_name='istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig.policy', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jwt_output_payload_locations', full_name='istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig.jwt_output_payload_locations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skip_validate_trust_domain', full_name='istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig.skip_validate_trust_domain', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FILTERCONFIG_JWTOUTPUTPAYLOADLOCATIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=444,
)

_FILTERCONFIG_JWTOUTPUTPAYLOADLOCATIONSENTRY.containing_type = _FILTERCONFIG
_FILTERCONFIG.fields_by_name['policy'].message_type = authentication_dot_v1alpha1_dot_policy__pb2._POLICY
_FILTERCONFIG.fields_by_name['jwt_output_payload_locations'].message_type = _FILTERCONFIG_JWTOUTPUTPAYLOADLOCATIONSENTRY
DESCRIPTOR.message_types_by_name['FilterConfig'] = _FILTERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FilterConfig = _reflection.GeneratedProtocolMessageType('FilterConfig', (_message.Message,), dict(

  JwtOutputPayloadLocationsEntry = _reflection.GeneratedProtocolMessageType('JwtOutputPayloadLocationsEntry', (_message.Message,), dict(
    DESCRIPTOR = _FILTERCONFIG_JWTOUTPUTPAYLOADLOCATIONSENTRY,
    __module__ = 'envoy.config.filter.http.authn.v2alpha1.config_pb2'
    # @@protoc_insertion_point(class_scope:istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig.JwtOutputPayloadLocationsEntry)
    ))
  ,
  DESCRIPTOR = _FILTERCONFIG,
  __module__ = 'envoy.config.filter.http.authn.v2alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:istio.envoy.config.filter.http.authn.v2alpha1.FilterConfig)
  ))
_sym_db.RegisterMessage(FilterConfig)
_sym_db.RegisterMessage(FilterConfig.JwtOutputPayloadLocationsEntry)


DESCRIPTOR._options = None
_FILTERCONFIG_JWTOUTPUTPAYLOADLOCATIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
