import grpc 
from proto import user_pb2

from app.core.db.models.post import Post

async def check_in_db(
    db:Post|None,
    context,
)->None:
    
    if db is None:
        await context.abort(grpc.StatusCode.NOT_FOUND, "Not found")
    return None