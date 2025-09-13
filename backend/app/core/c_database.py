from app.core import c_config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

USERNAME: str = c_config.database.USERNAME
PASSWORD: str = c_config.database.PASSWORD
DATABASE: str = c_config.database.DATABASE
HOST: str = c_config.database.HOST
PORT: int = c_config.database.PORT

DATABASE_URL = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL)
with engine.begin() as conn:
    conn.exec_driver_sql('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    conn.exec_driver_sql("CREATE EXTENSION IF NOT EXISTS citext;")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()