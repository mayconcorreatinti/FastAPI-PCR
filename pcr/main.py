from fastapi import FastAPI
from pcr.routers.recipes import app as recipes
from pcr.routers.users import app as users


app = FastAPI()

@app.get("/") 
def root():
    return "hello world"

app.include_router(recipes)
app.include_router(users)