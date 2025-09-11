from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    USERNAME: str = os.getenv("DB_USERNAME")
    PASSWORD: str = os.getenv("DB_PASSWORD")
    DATABASE: str = os.getenv("DB_DATABASE")
    HOST: str = os.getenv("DB_HOST")
    PORT: int = os.getenv("DB_PORT")

database = Database()