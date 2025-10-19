from fastapi import APIRouter
from src.models.users import User,UserResponse
from src.database import Mysqldb


app = APIRouter(tags=["users"],prefix="/users")
db = Mysqldb()

@app.post('/',response_model=UserResponse)
def register_user(account:User):
    user = db.select_user_from_table(account.username,account.email)
    return user
    