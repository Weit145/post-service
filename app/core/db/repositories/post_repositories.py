import grpc
from sqlalchemy import select

from ..db_hellper import db_helper
from ..models.post import Post
from .ipost_repositories import IPostRepository

class SQLAlchemyPostRepository(IPostRepository):
    
    async def create_post(self, post: Post) -> None:
        try:
            async with db_helper.transaction() as session:
                session.add(post)
        except Exception as e:
            raise
    
    async def get_post_by_id(self, id: int) -> Post | None:
        async with db_helper.transaction() as session:
            result = await session.get(Post, id)
            return result
    
    async def get_post_by_id_auth(self,id_auth) -> list[Post| None]:
        async with db_helper.transaction() as session:
            result = await session.execute(select(Post).where(Post.id_auth==id_auth))
            return result.scalars().all()
        
    async def get_posts_group(self, limit: int, last_id: int) -> list[Post]:
        async with db_helper.transaction() as session:
            stmt = (
                select(Post).order_by(Post.id.desc()).limit(limit)
            )
            if last_id > 0:
                stmt = stmt.where(Post.id < last_id)
            result = await session.execute(stmt)
            return result.scalars().all()
    
    async def delete_post(self, post: Post,context) -> None:
        async with db_helper.transaction() as session:
            await session.delete(post)

    async def update_post(self, post: Post,context) -> None:
        async with db_helper.transaction() as session:
            session.add(post)