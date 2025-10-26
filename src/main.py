from fastapi import FastAPI
from src.routers.recipes import app as recipes
from src.routers.users import app as users


app = FastAPI()

@app.get("/") 
def root():
    return "hello world"

app.include_router(recipes)
app.include_router(users)