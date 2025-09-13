from typing import Union
import bcrypt


class UtilPassword:
    @staticmethod
    def verify_password(
        raw_password: Union[str, bytes], hashed_password: bytes
    ) -> bool:
        password_attempt: bytes = b""

        if isinstance(raw_password, str):
            password_attempt: bytes = raw_password.encode("utf-8")

        return bcrypt.checkpw(
            password=password_attempt, hashed_password=hashed_password
        )

    @staticmethod
    def hash_password(raw_password: Union[str, bytes]) -> bytes:
        password_attempt: bytes = b""

        if isinstance(raw_password, str):
            password_attempt = raw_password.encode("utf-8")

        salt: bytes = bcrypt.gensalt()

        return bcrypt.hashpw(password_attempt, salt)

util_password = UtilPassword()