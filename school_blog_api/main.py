# Entry point of the app
import uvicorn
from fastapi import FastAPI
from routes import blog

app = FastAPI()

app.include_router(blog.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)