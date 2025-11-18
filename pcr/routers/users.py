from fastapi import APIRouter,HTTPException
from pcr.models.users import User,UserResponse
from pcr.database import Mysqldb
from http import HTTPStatus
from pcr.security import hash


app = APIRouter(tags=["users"],prefix="/users")
db = Mysqldb()

@app.post('/',response_model = UserResponse)
async def register_user(account:User):
    user = await db.select_user_from_table(account.username,account.email)
    if user:
        if user["username"] == account.username:
            raise HTTPException(
                detail = "This name already exists!",
                status_code = HTTPStatus.CONFLICT
            )
        elif user["email"] == account.email:
            raise HTTPException(
                detail = "This email already exists!",
                status_code = HTTPStatus.CONFLICT
            )
    
    await db.insert_user_from_table(
        (
            account.username,
            account.email,
            hash(account.password)
        )
    )

    user = await db.select_user_from_table(account.username)
    return {
        "id":user["id"],
        "username":user["username"],
        "email":user["email"]
    }

    
    