from fastapi import APIRouter
import json


app = APIRouter(tags=["recipes"],prefix="/recipes")

@app.get("/")
def get_recipes():
    with open("src/recipes.json","r",encoding='utf8') as file:
        return json.load(file)