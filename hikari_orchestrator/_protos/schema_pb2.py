# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"-\n\x0bInstruction\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.InstructionType\"\x1b\n\x07ShardId\x12\x10\n\x08shard_id\x18\x01 \x01(\x03\"\xb7\x01\n\x05Shard\x12\x1a\n\x05state\x18\x01 \x01(\x0e\x32\x0b.ShardState\x12-\n\tlast_seen\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07latency\x18\x03 \x01(\x01\x12\x17\n\nsession_id\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03seq\x18\x05 \x01(\x03H\x01\x88\x01\x01\x12\x10\n\x08shard_id\x18\x06 \x01(\x03\x42\r\n\x0b_session_idB\x06\n\x04_seq\"U\n\x10\x44isconnectResult\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.StatusType\x12\x1a\n\x05state\x18\x02 \x01(\x0b\x32\x06.ShardH\x00\x88\x01\x01\x42\x08\n\x06_state*!\n\x0fInstructionType\x12\x0e\n\nDISCONNECT\x10\x00*E\n\nShardState\x12\x0f\n\x0bNOT_STARTED\x10\x00\x12\x0c\n\x08STARTING\x10\x01\x12\x0b\n\x07STARTED\x10\x02\x12\x0b\n\x07STOPPED\x10\x03*%\n\nStatusType\x12\n\n\x06\x46\x41ILED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x02\x32\x82\x01\n\x0cOrchestrator\x12%\n\x07\x41\x63quire\x12\x06.Shard\x1a\x0c.Instruction\"\x00(\x01\x30\x01\x12+\n\nDisconnect\x12\x08.ShardId\x1a\x11.DisconnectResult\"\x00\x12\x1e\n\x08GetState\x12\x08.ShardId\x1a\x06.Shard\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'schema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_INSTRUCTIONTYPE']._serialized_start=398
  _globals['_INSTRUCTIONTYPE']._serialized_end=431
  _globals['_SHARDSTATE']._serialized_start=433
  _globals['_SHARDSTATE']._serialized_end=502
  _globals['_STATUSTYPE']._serialized_start=504
  _globals['_STATUSTYPE']._serialized_end=541
  _globals['_INSTRUCTION']._serialized_start=49
  _globals['_INSTRUCTION']._serialized_end=94
  _globals['_SHARDID']._serialized_start=96
  _globals['_SHARDID']._serialized_end=123
  _globals['_SHARD']._serialized_start=126
  _globals['_SHARD']._serialized_end=309
  _globals['_DISCONNECTRESULT']._serialized_start=311
  _globals['_DISCONNECTRESULT']._serialized_end=396
  _globals['_ORCHESTRATOR']._serialized_start=544
  _globals['_ORCHESTRATOR']._serialized_end=674
# @@protoc_insertion_point(module_scope)