from fastapi import APIRouter


app = APIRouter(tags=["users"],prefix="/users")

@app.post('/')
def register_user():
    ...