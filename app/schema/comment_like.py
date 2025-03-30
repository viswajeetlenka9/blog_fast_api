from pydantic import BaseModel

class CommentLikeResponse(BaseModel):
    id: int
    user_id: int
    comment_id: int

    class Config:
        from_attributes = True
