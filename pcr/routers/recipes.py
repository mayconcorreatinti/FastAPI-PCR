from fastapi import APIRouter,Body
from pcr.models.recipes import Recipe
from typing import Annotated
import json


app = APIRouter(tags=["recipes"],prefix="/recipes")

@app.get("/")
def get_recipes():
    with open("pcr/recipes.json","r",encoding='utf8') as file:
        return json.load(file)

@app.post("/")
def post_recipe(
    recipe: Annotated[
        Recipe,
        Body(
            examples=[
                {
                    "title": "Doce de leite",
                    "description": "...",
                    "ingredients": [
                        {
                            "ingredient 1":"leite",
                            "quantity": "2 litros"
                        },
                        {
                            "ingredient 2":"açúcar",
                            "quantity": "4 xícaras"
                        }
                    ],
                    "instructions": [
                        {
                            "instruction 1": "Coloque o leite e o açúcar em uma panela"
                        },
                        {
                            "instruction 2": "..."
                        }
                    ],
                    "serve": "...",
                    "difficulty": "easy",
                }
            ]
        )
    ]
):
    ...