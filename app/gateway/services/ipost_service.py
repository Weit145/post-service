from abc import ABC, abstractmethod
from proto import post_pb2

class IPostServiceImpl(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def CreatePost(self, request,context)->post_pb2.PostOutResponse:
        pass

    @abstractmethod
    async def DeletePost(self, request,context)->post_pb2.Empty:
        pass

    @abstractmethod
    async def GetGroupPost(self, request,context)->post_pb2.PostListResponse:
        pass

    @abstractmethod
    async def GetByIdPost(self, request,context)->post_pb2.PostOutResponse:
        pass

    @abstractmethod
    async def GetByUsernamePost(self, request,context)->post_pb2.PostListResponse:
        pass

    @abstractmethod
    async def PutPost(self, request,context)->post_pb2.PostOutResponse:
        pass