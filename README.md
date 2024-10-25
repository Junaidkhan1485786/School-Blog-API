# School-Blog-API(task:Luit Valley Technologies)
This is a FastAPI project for creating and managing a school blog with MongoDB as the database. Data validation is handled with Pydantic, ensuring consistent data quality.

## Features
Create, Read blog posts.
MongoDB Integration using Motor.
Data Validation with Pydantic models.
API Endpoints for blog creation and retrieval.

## 🛠️ Installation
Clone the Repository
```
git clone https://github.com/username/school_blog_api.git 
cd school_blog_api
```





## Install Dependencies
``` 
pip install fastapi motor pydantic uvicorn
```

## project structure
```
school_blog_api/
├── main.py            # Entry point of the app
├── models.py          # Pydantic models for data validation
├── database.py        # MongoDB connection setup
└── routes/
    └── blog.py        # Blog-related endpoints
```
