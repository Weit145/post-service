from proto import post_pb2_grpc

from app.gateway.services.post_service import PostServiceImpl


class PostServicer(post_pb2_grpc.PostServicer):
    async def CreatePost(self, request, context):
        return await PostServiceImpl().CreatePost(request, context)

    async def DeletePost(self, request, context):
        return await PostServiceImpl().DeletePost(request, context)

    async def GetGroupPost(self, request, context):
        return await PostServiceImpl().GetGroupPost(request, context)

    async def GetByIdPost(self, request, context):
        return await PostServiceImpl().GetByIdPost(request, context)

    async def GetByIdUserPost(self, request, context):
        return await PostServiceImpl().GetByIdUserPost(request, context)

    async def PutPost(self, request, context):
        return await PostServiceImpl().PutPost(request, context)
