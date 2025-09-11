from app.core import c_database
from app.models import m_control
from app.schemas import sc_users
from app.utils import u_password

session = c_database.SessionLocal()

def handle_signup(payload: sc_users.SignUp):
    try:
        full_name: str = payload.full_name
        username: str = payload.username
        email: str = payload.email
        password_hash: str = u_password.password_hasher(payload.password)
        role: str = payload.role

        new_user = m_control.User(
            username=username,
            email=email,
            password_hash=password_hash,
            full_name=full_name,
            role=role,
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        
        return True
    except Exception as e:
        print("Error: ", e)
        return False
    
    finally:
        session.close()