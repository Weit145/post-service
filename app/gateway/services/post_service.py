from app.core.db.models.post import Post
from proto import post_pb2_grpc, post_pb2

from app.core.db.repositories.post_repositories import SQLAlchemyPostRepository
from app.gateway.services.ipost_service import IPostServiceImpl
# from app.kafka.repositories.kafka_repositories import KafkaRepository
from app.user_service.grpc.user_service import UserService
from app.gateway.utils.checks import (
    check_in_db,
    check_auth_post
)
from app.gateway.utils.convert import (
    convert_post_create_request,
    convert_post_out_response,
)

class PostServiceImpl(IPostServiceImpl):
    def __init__(self):
        self.user = UserService()
        self.repo = SQLAlchemyPostRepository()
        # self.kf = KafkaRepository()


    async def CreatePost(self, request, context) -> post_pb2.PostOutResponse:
        new_post = convert_post_create_request(request)
        await self.repo.create_post(new_post)
        username = await self.user.get_user_by_id(request.auth_id)
        return convert_post_out_response(new_post, username)
    
    async def DeletePost(self, request, context) -> post_pb2.Empty:
        post_to_delete = await self.repo.get_post_by_id(request.post_id)
        await check_in_db(post_to_delete, context)
        await check_auth_post(post_to_delete, request.auth_id, context)

        await self.repo.delete_post(post_to_delete,context)
        return post_pb2.Empty()
    
    async def GetGroupPost(self, request, context) -> post_pb2.PostListResponse:
        posts = await self.repo.get_posts_group(request.limit, request.last_id)
        await check_in_db(posts, context)
        list_response = []
        auth_ids = list({post.id_auth for post in posts})
        users_map = await self.user.get_users_by_ids(auth_ids)
        await check_in_db(users_map, context)
        for post in posts:
            username = users_map.get(post.id_auth, "unknown")
            post_response = convert_post_out_response(post, username)
            list_response.append(post_response)
        return post_pb2.PostListResponse(posts=list_response)
    
    async def GetByIdPost(self, request, context) -> post_pb2.PostOutResponse:
        post = await self.repo.get_post_by_id(request.post_id)
        await check_in_db(post, context)
        username = await self.user.get_user_by_id(post.id_auth)
        await check_in_db(username, context)
        return convert_post_out_response(post, username)
    
    async def GetByUsernamePost(self, request, context) -> post_pb2.PostListResponse:
        auth_id = await self.user.get_user_by_username(request.username)
        await check_in_db(auth_id, context)
        posts = await self.repo.get_post_by_id_auth(auth_id)
        await check_in_db(posts, context)
        list_response = []
        for post in posts:
            post_response = convert_post_out_response(post, request.username)
            list_response.append(post_response)
        return post_pb2.PostListResponse(posts=list_response)
    
    async def PutPost(self, request, context) -> post_pb2.PostOutResponse:
        post = await self.repo.get_post_by_id(request.post_id)
        await check_in_db(post, context)
        await check_auth_post(post, request.auth_id, context)

        post.title = request.title
        post.body = request.body

        await self.repo.update_post(post,context)
        username = await self.user.get_user_by_id(request.auth_id)
        return convert_post_out_response(post, username)
    
    async def DeletePostFromUserService(self, data:dict)->None:
        id = data.get("id")
        posts = await self.repo.get_post_by_id_auth(id)
        if posts is not None:
            await self.repo.delete_posts(posts)