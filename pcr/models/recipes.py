from pydantic import BaseModel,Field
from typing import List,Dict


class Recipe(BaseModel):
    title: str
    description: str 
    ingredients: List[Dict] 
    instructions: List[Dict]
    serve: str
    difficulty: str