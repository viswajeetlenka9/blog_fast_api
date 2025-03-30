from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.base.base import get_db
from app.models import Posts, Users, Likes
from app.schema import LikeResponse
from app.auth import get_current_user

router = APIRouter(tags=["likes"])

# 👍 Like a Post
@router.post("/posts/{post_id}/like", response_model=LikeResponse)
def like_post(post_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    post = db.query(Posts).filter(Posts.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    existing_like = db.query(Likes).filter(Likes.user_id == current_user.id, Likes.post_id == post_id).first()
    if existing_like:
        raise HTTPException(status_code=400, detail="You have already liked this post")
    
    new_like = Likes(user_id=current_user.id, post_id=post_id)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)

    return new_like

# ❌ Unlike a Post
@router.delete("/posts/{post_id}/like")
def unlike_post(post_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    like = db.query(Likes).filter(Likes.user_id == current_user.id, Likes.post_id == post_id).first()
    if not like:
        raise HTTPException(status_code=400, detail="You haven't liked this post")

    db.delete(like)
    db.commit()
    return {"message": "Like removed"}