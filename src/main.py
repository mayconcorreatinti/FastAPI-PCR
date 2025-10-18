from fastapi import FastAPI
from src.routers.recipes import app as recipes


app = FastAPI()

@app.get("/")
def root():
    return "hello world"

app.include_router(recipes)