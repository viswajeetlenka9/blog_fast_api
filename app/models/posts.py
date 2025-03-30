from sqlalchemy import (Column, INT, String, Text, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from datetime import datetime
from app.base.base import Base

class Posts(Base):
    __tablename__ = "posts"

    id = Column(INT, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True, default=None)
    owner_id = Column(INT, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="posts")
    likes = relationship("Likes", back_populates="post", cascade="all, delete")
    comments = relationship("Comments", back_populates="post", cascade="all, delete")