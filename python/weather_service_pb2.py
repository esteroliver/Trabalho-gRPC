# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: weather_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'weather_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15weather_service.proto\x12\x07weather\"5\n\x0eWeatherRequest\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\"\"\n\x0fWeatherResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2Q\n\x0eWeatherService\x12?\n\nGetWeather\x12\x17.weather.WeatherRequest\x1a\x18.weather.WeatherResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'weather_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WEATHERREQUEST']._serialized_start=34
  _globals['_WEATHERREQUEST']._serialized_end=87
  _globals['_WEATHERRESPONSE']._serialized_start=89
  _globals['_WEATHERRESPONSE']._serialized_end=123
  _globals['_WEATHERSERVICE']._serialized_start=125
  _globals['_WEATHERSERVICE']._serialized_end=206
# @@protoc_insertion_point(module_scope)
