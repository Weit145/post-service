from app.core.db.models.post import Post
from proto import post_pb2_grpc, post_pb2

from app.core.db.repositories.post_repositories import SQLAlchemyPostRepository
from app.gateway.services.ipost_service import IPostServiceImpl
# from app.kafka.repositories.kafka_repositories import KafkaRepository

from app.gateway.utils.checks import (
    check_in_db,
)

class PostServiceImpl(IPostServiceImpl):
    def __init__(self):
        self.repo = SQLAlchemyPostRepository()
        # self.kf = KafkaRepository()


    async def CreatePost(self, request, context) -> post_pb2.PostOutResponse:
        new_post = Post(
            title=request.title,
            body=request.body,
            id_auth=request.auth_id,
        )

        await self.repo.create_post(new_post)

        return await super().CreatePost(request, context)
    
    async def DeletePost(self, request, context) -> post_pb2.Empty:
        return await super().DeletePost(request, context)
    
    async def GetGroupPost(self, request, context) -> post_pb2.PostListResponse:
        return await super().GetGroupPost(request, context)
    
    async def GetByIdPost(self, request, context) -> post_pb2.PostOutResponse:
        return await super().GetByIdPost(request, context)
    
    async def GetByUsernamePost(self, request, context) -> post_pb2.PostListResponse:
        return await super().GetByUsernamePost(request, context)
    
    async def PutPost(self, request, context) -> post_pb2.PostOutResponse:
        return await super().PutPost(request, context)
