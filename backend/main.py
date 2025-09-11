from app.core import c_database
from app.api import a_auth

import argparse

import fastapi
import uvicorn

app = fastapi.FastAPI()

app.include_router(a_auth.router, prefix="/auth", tags=["auth"])

# Argparse
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8001)

    from app.models import m_control
    _ = m_control

    parser = argparse.ArgumentParser()

    parser.add_argument('--migrate', action='store_true', help='Run migrations')
    parser.add_argument('--migrate-fresh', action='store_true', help="Drop and run migrations")
    args = parser.parse_args()

    if args.migrate:
        print("Tables found:", c_database.Base.metadata.tables.keys())
        print("Migrating...")
        c_database.Base.metadata.create_all(bind=c_database.engine)
        print("Migration completed.")
        
    elif args.migrate_fresh:
        print("Dropping all tables...")
        c_database.Base.metadata.drop_all(bind=c_database.engine)
        print("Tables dropped.")
        print("Migrating...")
        c_database.Base.metadata.create_all(bind=c_database.engine)
        print("Migration completed.")

