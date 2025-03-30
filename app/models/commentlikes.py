from sqlalchemy import (Column, INT, ForeignKey, UniqueConstraint)
from sqlalchemy.orm import relationship
from app.base.base import Base

class CommentLikes(Base):
    __tablename__ = "comment_likes"

    id = Column(INT, primary_key=True, index=True)
    user_id = Column(INT, ForeignKey("users.id"))
    comment_id = Column(INT, ForeignKey("comments.id"))

    user = relationship("Users", back_populates="comment_likes")
    comment = relationship("Comments", back_populates="likes")

    __table_args__ = (UniqueConstraint("user_id", "comment_id", name="unique_comment_like"),)