import grpc
from proto import user_post_pb2_grpc, user_post_pb2

from app.user_service.grpc.iuser_service import IUserService


class UserService(IUserService):

    def __init__(self, host: str = "user-service", port: int = 50055) -> None:
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = user_post_pb2_grpc.UserPostStub(self.channel)

    async def get_user_by_username(self, username: str)-> int:
        request = user_post_pb2.GetByUsernameRequest(username=username)
        response = await self.stub.GetByUsername(request)
        return response.id
    
    async def get_user_by_id(self, user_id: int)-> str:
        request = user_post_pb2.GetByIdRequest(id=user_id)
        response = await self.stub.GetByID(request)
        return response.username
    
    async def get_users_by_ids(self, user_ids: list[int]) -> dict[int, str]:
        request = user_post_pb2.GetByIdsRequest(ids=user_ids)
        response = await self.stub.GetByIDs(request)
        return response.users