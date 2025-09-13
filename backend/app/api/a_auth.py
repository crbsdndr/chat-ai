from fastapi import APIRouter, HTTPException


from app.core import c_database
from app.core import c_models
from app.schemas import sc_users, sc_abstract
from app.services import s_user

router = APIRouter()


@router.post("/signup/")
def signup(payload: sc_users.SignUp):
    try:
        new_auth: s_user.Auth = s_user.Auth(
            session=c_database.SessionLocal(),
            model=c_models.User
        )

        if new_auth.handle_signup(payload=payload):
            return sc_abstract.HTTPSuccessful(status_code=200, detail="Sign Up successful!")

    except Exception as ex:
        HTTPException(status_code=400, detail=str(ex))
