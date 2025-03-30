from sqlalchemy import (Column, INT, ForeignKey, UniqueConstraint)
from sqlalchemy.orm import relationship
from app.base.base import Base

class Likes(Base):
    __tablename__ = "likes"

    id = Column(INT, primary_key=True, index=True)
    user_id = Column(INT, ForeignKey("users.id"))
    post_id = Column(INT, ForeignKey("posts.id"))

    user = relationship("Users", back_populates="likes")
    post = relationship("Posts", back_populates="likes")

    __table_args__ = (UniqueConstraint("user_id", "post_id", name="unique_like"),)