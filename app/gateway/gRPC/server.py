import grpc
from proto import post_pb2_grpc, post_pb2

from app.gateway.gRPC.post_server import PostServicer

async def serve():
    server = grpc.aio.server()
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:50054')
    print("gRPC сервер запущен на порту 50054...")
    await server.start()
    await server.wait_for_termination()
