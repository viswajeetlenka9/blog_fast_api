from sqlalchemy import (Column, INT, String, Text, Boolean, DateTime)
from sqlalchemy.orm import relationship
from datetime import datetime
from app.base.base import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(INT, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    password = Column(Text, nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    email = Column(String(50), nullable=False, unique=True, index=True)
    is_active = Column(Boolean, default=False, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True, default=None)

    posts = relationship("Posts", back_populates="owner")
    likes = relationship("Likes", back_populates="user", cascade="all, delete")
    comments = relationship("Comments", back_populates="user", cascade="all, delete")
    comment_likes = relationship("CommentLikes", back_populates="user", cascade="all, delete")