from fastapi import FastAPI
from app.api.v1.endpoints.auth import auth_router

app = FastAPI()
app.include_router(auth_router)

@app.get("/")
def hello():
    return {"message": "hello world!"}