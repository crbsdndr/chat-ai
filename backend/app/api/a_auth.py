from fastapi import APIRouter, HTTPException


from app.core import c_models
from app.services import s_user
from app.core import c_database
from app.schemas import sc_users

router = APIRouter()


@router.post("/signup/")
def signup(payload: sc_users.SignUp):
    new_auth = s_user.Auth(session=c_database.SessionLocal(), model=c_models.User)
    result = new_auth.insert_new(payload=payload)

    if result:
        return {"detail": "Sign Up sucessful"}
    else:
        return {"detail": "How did you get here? Contact Us!"}


@router.post("/login/")
def login(payload: sc_users.LogIn):
    if not (bool(payload.email) ^ bool(payload.username)):
        return HTTPException(
            status_code=400,
            detail="Please fill in one of the fields (username or email)",
        )
    new_auth = s_user.Auth(session=c_database.SessionLocal(), model=c_models.User)
    result = new_auth.handle_login(payload=payload)

    if result:
        return {"detail": "Log In sucessful"}
    else:
        return {"detail": "How did you get here? Contact Us!"}
