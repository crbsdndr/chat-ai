from typing import Union
import bcrypt


class UtilPassword:
    @staticmethod
    def verify_password(raw_password: Union[str, bytes], hashed_password: Union[str, bytes]) -> bool:
        if isinstance(raw_password, str):
            password_attempt = raw_password.encode("utf-8")
        else:
            password_attempt = raw_password

        if isinstance(hashed_password, str):
            hashed_password_bytes = hashed_password.encode("utf-8")
        else:
            hashed_password_bytes = hashed_password

        return bcrypt.checkpw(password_attempt, hashed_password_bytes)

    @staticmethod
    def hash_password(raw_password: Union[str, bytes]) -> str:
        if isinstance(raw_password, str):
            password_attempt = raw_password.encode("utf-8")
        else:
            password_attempt = raw_password
            
        hashed_bytes = bcrypt.hashpw(password_attempt, bcrypt.gensalt())
        return hashed_bytes.decode("utf-8") 

util_password = UtilPassword()
