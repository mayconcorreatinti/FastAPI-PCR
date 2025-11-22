from fastapi import APIRouter,Body
from pcr.models.recipes import Recipe,RecipeResponse
import json


app = APIRouter(tags=["recipes"],prefix="/recipes")

@app.get("/")
def get_recipes():
    with open("pcr/recipes.json","r",encoding='utf8') as file:
        return json.load(file)

@app.post("/",response_model = RecipeResponse)
def post_recipe(recipe: Recipe):
    ...