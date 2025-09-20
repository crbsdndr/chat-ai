import jwt
import datetime
from datetime import timezone

SECRET_KEY = "your-secret-key-here"

def create_jwt_token(payload_data, expires_minutes=30):
    payload = {
        **payload_data,
        'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.now(tz=timezone.utc)
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token telah kadaluarsa"}
    except jwt.InvalidTokenError:
        return {"error": "Token tidak valid"}

user_data = {
    'user_id': 123,
    'username': 'john_doe',
    'email': 'john@example.com'
}

token = create_jwt_token(user_data)

print(f"Generated Token: {token}")
print(f"Decoded Payload: ", verify_jwt_token(token=token))