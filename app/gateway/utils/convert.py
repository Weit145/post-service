from proto import post_pb2

from app.core.db.models.post import Post

def convert_post_create_request(
    request,
)->Post:
    return Post(
        title=request.title,
        body=request.body,
        id_auth=request.auth_id,
    )

def convert_post_out_response(
    post:Post,
    username:str,
)->post_pb2.PostOutResponse:
    return post_pb2.PostOutResponse(
        post_id=post.id,
        title=post.title,
        body=post.body,
        username=username,
    )