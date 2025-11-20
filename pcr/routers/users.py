from fastapi import APIRouter,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from pcr.models.users import User,UserResponse,Token,Message,FormData
from pcr.database import Mysqldb
from http import HTTPStatus
from pcr.security import (
    hash,verify_password,create_access_token,get_current_user,verify_credentials
)
from typing import Annotated


app = APIRouter(tags=["users"],prefix="/users")
db = Mysqldb()

@app.post("/",response_model = UserResponse)
async def register_user(account:User):
    await verify_credentials(
        account.username,
        account.email
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

@app.post("/token",response_model = Token)
async def create_token(
    form_data : Annotated[OAuth2PasswordRequestForm,Depends()]
):
    user = await db.select_user_from_table(email=form_data.username)
    if not user or not verify_password(form_data.password,user["password"]):
        raise HTTPException(
            detail = "Incorrect username or password!",
            status_code = HTTPStatus.FORBIDDEN
        )
    token = create_access_token({"sub":form_data.username})
    return {
        "access_token":token,
        "token_type": "Bearer"
    }

@app.delete("/{id}",response_model = Message)
async def delete_user(id:int,authenticated_user = Depends(get_current_user)):
    if id != authenticated_user["id"]:
        raise HTTPException(
            status_code = HTTPStatus.UNAUTHORIZED,
            detail = "unauthorized request"
        )
    await db.delete_user_from_table((id,))
    return {"Message": "User deleted!"}

@app.put("/{id}",response_model = Message)
async def update_user(
id:int,account:User,authenticated_user = Depends(get_current_user)
):
    if id != authenticated_user["id"]:
        raise HTTPException(
            status_code = HTTPStatus.UNAUTHORIZED,
            detail = "unauthorized request"
        )
    user = await db.select_user_from_table(
        username=account.username,
        email=account.email
    )
    await verify_credentials(
        account.username,
        account.email
    )
    await db.update_user_from_table(
        (
            account.username,
            account.email,
            account.password,
            id
        )
    )
    return {"Message":"updated user"}
    