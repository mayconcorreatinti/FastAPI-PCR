from fastapi import APIRouter,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from pcr.models.users import User,UserResponse,Token
from pcr.database import Mysqldb
from http import HTTPStatus
from pcr.security import hash,verify_password,create_access_token
from typing import Annotated


app = APIRouter(tags=["users"],prefix="/users")
db = Mysqldb()

@app.post("/",response_model = UserResponse)
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
    
    await db.insert_user_into_table(
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

@app.post("/token",response_model = Token )
async def create_token(
    form_data : Annotated[OAuth2PasswordRequestForm,Depends()]
):
    user = await db.select_user_from_table(email=form_data.username)
    if not user or not verify_password(form_data.password,user["password"]):
        raise HTTPException(
            detail = "Incorrect username or password!",
            status_code = HTTPStatus.FORBIDDEN
        )
    
    token = create_access_token({"email":form_data.username})
    return {
        "access_token":token,
        "token_type": "Bearer"
    }


    