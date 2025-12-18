import grpc
from proto import post_pb2_grpc

from app.gateway.gRPC.post_server import PostServicer


async def serve():
    server = grpc.aio.server()
    post_pb2_grpc.add_PostServicer_to_server(PostServicer(), server)
    server.add_insecure_port("[::]:50054")
    print("gRPC сервер запущен на порту 50054...")
    await server.start()
    await server.wait_for_termination()
