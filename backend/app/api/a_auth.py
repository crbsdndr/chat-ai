from fastapi import APIRouter, HTTPException


from app.core import c_models
from app.services import s_user
from app.core import c_database
from app.schemas import sc_users

router = APIRouter()

@router.post("/signup/")
def signup(payload: sc_users.SignUp):
    try:
        new_auth = s_user.Auth(
            session=c_database.SessionLocal(),
            model=c_models.User
        )
        
        new_auth.handle_signup(payload=payload)
        return {"detail": "Signup sucessful"}
    
    except HTTPException:
        raise

    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(ex)}")

@router.post("/login/")
def login(payload: sc_users.LogIn):
    try:
        if payload.username and payload.email:
            return HTTPException(status_code=400, detail="Please fill in one of the fields (username or email)")


    except Exception as ex:
        HTTPException(status_code=400, detail=str(ex))