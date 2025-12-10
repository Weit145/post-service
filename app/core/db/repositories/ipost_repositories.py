from abc import ABC, abstractmethod

from ..models.post import Post

class IPostRepository(ABC):

    @abstractmethod
    async def create_post(self, post: Post) -> None:
        pass

    @abstractmethod
    async def get_post_by_id(self, id: int) -> Post | None:
        pass

    @abstractmethod
    async def get_post_by_id_auth(self,id_auth) -> list[Post| None]:
        pass
    
    @abstractmethod
    async def delete_post(self, post: Post) -> None:
        pass

    @abstractmethod
    async def delete_posts(self, posts:list[Post])->None:
        pass

    @abstractmethod
    async def update_post(self, post: Post,context) -> None:
        pass