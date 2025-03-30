from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.base.base import get_db
from app.models import Posts, Users, Comments
from app.schema import PostCreate, PostResponse, CommentCreate, CommentResponse
from app.auth import get_current_user

router = APIRouter(prefix="/posts", tags=["posts"])

# 📝 Create a Post
@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    new_post = Posts(**post.model_dump(), owner_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# 📌 Get All Posts
@router.get("/", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return db.query(Posts).all()

# 🔍 Get a Specific Post
@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    post = db.query(Posts).filter(Posts.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# ✏️ Update a Post
@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post_data: PostCreate, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    post = db.query(Posts).filter(Posts.id == post_id, Posts.owner_id == current_user.id).first()
    if not post:
        raise HTTPException(status_code=403, detail="Not authorized or post does not exist")
    
    for key, value in post_data.model_dump().items():
        setattr(post, key, value)
    post.updated_at = datetime.utcnow
    
    db.commit()
    db.refresh(post)
    return post

# ❌ Delete a Post
@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    post = db.query(Posts).filter(Posts.id == post_id, Posts.owner_id == current_user.id).first()
    if not post:
        raise HTTPException(status_code=403, detail="Not authorized or post does not exist")
    
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}
