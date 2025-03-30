from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.base.base import get_db
from app.models import Posts, Users, Comments
from app.schema import CommentCreate, CommentResponse
from app.auth import get_current_user

router = APIRouter(tags=["comments"])

# 💬 Comment on a Post
@router.post("/posts/{post_id}/comment", response_model=CommentResponse)
def comment_on_post(post_id: int, comment_data: CommentCreate, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    post = db.query(Posts).filter(Posts.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    new_comment = Comments(content=comment_data.content, user_id=current_user.id, post_id=post_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


# 📝 Get all comments for a post
@router.get("/posts/{post_id}/comments", response_model=list[CommentResponse])
def get_comments(post_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return db.query(Comments).filter(Comments.post_id == post_id).all()
