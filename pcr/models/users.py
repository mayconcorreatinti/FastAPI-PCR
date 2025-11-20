from pydantic import BaseModel,EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class FormData(BaseModel):
    email: EmailStr
    password: str
    
class Message(BaseModel):
    Message: str