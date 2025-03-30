from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
    
class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    image_url: Optional[str]
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True
