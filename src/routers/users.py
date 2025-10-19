from fastapi import APIRouter
from src.schemas.users import User,UserResponse


app = APIRouter(tags=["users"],prefix="/users")

@app.post('/',response_model=UserResponse)
def register_user(account:User):
    user = {
        "id":2,
        "username":account.username,
        "email":account.email
    }
    return user