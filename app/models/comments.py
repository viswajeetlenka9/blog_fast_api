from sqlalchemy import (Column, INT, Text, DateTime, ForeignKey)
from datetime import datetime
from sqlalchemy.orm import relationship
from app.base.base import Base


class Comments(Base):
    __tablename__ = "comments"

    id = Column(INT, primary_key=True, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(INT, ForeignKey("users.id"))
    post_id = Column(INT, ForeignKey("posts.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True, default=None)

    user = relationship("Users", back_populates="comments")
    post = relationship("Posts", back_populates="comments")
    likes = relationship("CommentLikes", back_populates="comment", cascade="all, delete")