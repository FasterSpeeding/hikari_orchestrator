# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import schema_pb2 as schema__pb2


class OrchestratorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Acquire = channel.stream_stream(
                '/Orchestrator/Acquire',
                request_serializer=schema__pb2.Shard.SerializeToString,
                response_deserializer=schema__pb2.Instruction.FromString,
                )
        self.Disconnect = channel.unary_unary(
                '/Orchestrator/Disconnect',
                request_serializer=schema__pb2.ShardId.SerializeToString,
                response_deserializer=schema__pb2.DisconnectResult.FromString,
                )
        self.GetState = channel.unary_unary(
                '/Orchestrator/GetState',
                request_serializer=schema__pb2.ShardId.SerializeToString,
                response_deserializer=schema__pb2.Shard.FromString,
                )


class OrchestratorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Acquire(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrchestratorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Acquire': grpc.stream_stream_rpc_method_handler(
                    servicer.Acquire,
                    request_deserializer=schema__pb2.Shard.FromString,
                    response_serializer=schema__pb2.Instruction.SerializeToString,
            ),
            'Disconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.Disconnect,
                    request_deserializer=schema__pb2.ShardId.FromString,
                    response_serializer=schema__pb2.DisconnectResult.SerializeToString,
            ),
            'GetState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetState,
                    request_deserializer=schema__pb2.ShardId.FromString,
                    response_serializer=schema__pb2.Shard.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Orchestrator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Orchestrator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Acquire(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Orchestrator/Acquire',
            schema__pb2.Shard.SerializeToString,
            schema__pb2.Instruction.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Orchestrator/Disconnect',
            schema__pb2.ShardId.SerializeToString,
            schema__pb2.DisconnectResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Orchestrator/GetState',
            schema__pb2.ShardId.SerializeToString,
            schema__pb2.Shard.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)