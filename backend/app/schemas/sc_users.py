from pydantic import BaseModel, EmailStr, Field

class UserRole():
    user = "user"
    admin = "admin"
    superadmin = "superadmin"

class SignUp(BaseModel):
    full_name: str | None = Field(default=None, min_length=3, max_length=100)
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)
    role: str = Field(default=UserRole.user, pattern="^(user|admin|superadmin)$")

class LogIn(BaseModel):
    username: str | None
    email: str | None
    password: str = Field(min_length=8)