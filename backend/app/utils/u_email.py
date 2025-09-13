import re

class UtilEmail():

    @staticmethod
    def validate(email: str) -> bool:
        regex_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        if re.fullmatch(regex_pattern, email):
            return True
        else:
            return False
        

util_email = UtilEmail()