from app.schemas import sc_users
from app.utils import u_password, u_email

from typing import Union
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

class Auth:
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def show_by(self, email=None, username=None) -> Union[object, None]:
        model = self.model
        session = self.session
        result: Union[object, None] = None

        if email:
            result = session.query(model).filter_by(email=email).first()
    
        elif username:
            result = session.query(model).filter_by(username=username).first()

        return result
    
    def handle_signup(self, payload: sc_users.SignUp) -> None:
        try:
            full_name: str = payload.full_name
            username: str = payload.username
            email: str = payload.email
            password_hash: str = u_password.util_password.hash_password(payload.password)
            role: str = payload.role

            if not u_email.util_email.validate(email=email):
                raise HTTPException(status_code=501, detail="The email is in wrong format")

            new_user = self.model(
                username=username,
                email=email,
                password_hash=password_hash,
                full_name=full_name,
                role=role,
            )

            self.session.add(new_user)
            self.session.commit()
            self.session.refresh(new_user)

        except HTTPException:
            self.session.rollback()
            raise

        except IntegrityError:
            self.session.rollback()
            raise HTTPException(status_code=409, detail="Email or username already exists")

        except Exception as ex:
            self.session.rollback()
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(ex)}")

        finally:
            self.session.close()