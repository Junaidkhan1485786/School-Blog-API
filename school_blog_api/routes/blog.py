# Blog-related endpoints

from fastapi import APIRouter, HTTPException
from models import BlogPost
from database import db
from bson import ObjectId

router = APIRouter()

@router.post("/blog/", response_model=BlogPost)
async def create_blog(blog: BlogPost):
    blog.created_at = datetime.utcnow()
    result = await db.blogs.insert_one(blog.dict())
    if result.inserted_id:
        blog.id = result.inserted_id
        return blog
    raise HTTPException(status_code=500, detail="Failed to create blog post")

@router.get("/blogs/")
async def get_blogs():
    blogs = await db.blogs.find().to_list(100)
    return blogs
