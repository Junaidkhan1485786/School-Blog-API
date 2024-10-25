# Pydantic models for data validation

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BlogPost(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    content: str
    author: str
    created_at: Optional[datetime] = None