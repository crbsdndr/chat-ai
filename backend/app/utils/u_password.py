from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def password_hasher(password: str) -> str:
    return pwd_context.hash(password)