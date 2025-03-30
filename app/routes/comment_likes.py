from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.base.base import get_db
from app.models import Users, Comments, CommentLikes
from app.schema import CommentLikeResponse
from app.auth import get_current_user

router = APIRouter(tags=["comment_likes"])


# 👍 Like a Comment
@router.post("/comments/{comment_id}/like", response_model=CommentLikeResponse)
def like_comment(comment_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    comment = db.query(Comments).filter(Comments.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    existing_like = db.query(CommentLikes).filter(CommentLikes.user_id == current_user.id, CommentLikes.comment_id == comment_id).first()
    if existing_like:
        raise HTTPException(status_code=400, detail="You have already liked this comment")

    new_like = CommentLikes(user_id=current_user.id, comment_id=comment_id)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like

# ❌ Unlike a Comment
@router.delete("/comments/{comment_id}/like")
def unlike_comment(comment_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    like = db.query(CommentLikes).filter(CommentLikes.user_id == current_user.id, CommentLikes.comment_id == comment_id).first()
    if not like:
        raise HTTPException(status_code=400, detail="You haven't liked this comment")

    db.delete(like)
    db.commit()
    return {"message": "Like removed"}

# 🔢 Get Like Count for a Comment
@router.get("/comments/{comment_id}/likes_count")
def get_comment_likes_count(comment_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    count = db.query(CommentLikes).filter(CommentLikes.comment_id == comment_id).count()
    return {"comment_id": comment_id, "likes_count": count}