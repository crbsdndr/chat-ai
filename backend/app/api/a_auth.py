from fastapi import APIRouter

from app.schemas import sc_users
from app.services import s_auth

router = APIRouter()

@router.post("/signup/")
def signup(payload: sc_users.SignUp):
    return s_auth.handle_signup(payload)
