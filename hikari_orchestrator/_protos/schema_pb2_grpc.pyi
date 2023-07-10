import typing
from collections import abc as _collections

import grpc.aio  # type: ignore

from . import schema_pb2 as schema__pb2

class OrchestratorStub:
    def __init__(self, channel: grpc.Channel | grpc.aio.Channel) -> None: ...
    def Acquire(self) -> grpc.aio.StreamStreamCall[schema__pb2.Shard, schema__pb2.Instruction]: ...
    async def Disconnect(self, shard_id: schema__pb2.ShardId, /) -> schema__pb2.DisconnectResult: ...
    async def GetState(self, shard_id: schema__pb2.ShardId, /) -> schema__pb2.Shard: ...

class OrchestratorServicer:
    def Acquire(
        self, request_iterator: _collections.AsyncIterator[schema__pb2.Shard], context: grpc.ServicerContext
    ) -> _collections.AsyncIterator[schema__pb2.Instruction]: ...
    def Disconnect(
        self, request: schema__pb2.ShardId, context: grpc.ServicerContext
    ) -> schema__pb2.DisconnectResult: ...
    def GetState(self, request: schema__pb2.ShardId, context: grpc.ServicerContext) -> schema__pb2.Shard: ...

def add_OrchestratorServicer_to_server(servicer: OrchestratorServicer, server: grpc.Server | grpc.aio.Server) -> None: ...

# This class is part of an EXPERIMENTAL API.
class Orchestrator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Acquire(
        request_iterator: object,
        target: object,
        options: object = (),
        channel_credentials: object = None,
        call_credentials: object = None,
        insecure: object = False,
        compression: object = None,
        wait_for_ready: object = None,
        timeout: object = None,
        metadata: object = None,
    ) -> typing.Any: ...
    @staticmethod
    def Disconnect(
        request: object,
        target: object,
        options: object = (),
        channel_credentials: object = None,
        call_credentials: object = None,
        insecure: object = False,
        compression: object = None,
        wait_for_ready: object = None,
        timeout: object = None,
        metadata: object = None,
    ) -> typing.Any: ...
    @staticmethod
    def GetState(
        request: object,
        target: object,
        options: object = (),
        channel_credentials: object = None,
        call_credentials: object = None,
        insecure: object = False,
        compression: object = None,
        wait_for_ready: object = None,
        timeout: object = None,
        metadata: object = None,
    ) -> typing.Any: ...