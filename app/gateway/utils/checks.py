import grpc

from app.core.db.models.post import Post


async def check_in_db(
    db,
    context,
) -> None:
    if db is None:
        await context.abort(grpc.StatusCode.NOT_FOUND, "Not found")
    return None


async def check_auth_post(
    post: Post,
    auth_id: int,
    context,
) -> None:
    if post.id_auth != auth_id:
        await context.abort(grpc.StatusCode.PERMISSION_DENIED, "Permission denied")
    return None
