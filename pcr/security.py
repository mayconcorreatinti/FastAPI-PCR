# from pwdlib import PasswordHash 


# password_hash = PasswordHash.recommended()

from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

def hash(password: str):
    return fernet.encrypt(password.encode()).decode()

# def verify_password(password, hash):
#     return password_hash.verify(password, hash)


