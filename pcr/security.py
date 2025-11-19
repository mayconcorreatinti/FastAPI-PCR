from pwdlib import PasswordHash 
from pcr.database import Mysqldb
from datetime import datetime, timedelta, timezone
import os
import jwt


password_hash = PasswordHash.recommended()

def hash(password: str):
    return password_hash.hash(password)

def verify_password(password, hash):
    return password_hash.verify(password, hash)

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        os.getenv("SECRET_KEY"),
        algorithm=os.getenv("ALGORITHM")
    )
    return encoded_jwt


