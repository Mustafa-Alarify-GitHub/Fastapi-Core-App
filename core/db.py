from sqlmodel import SQLModel, create_engine, Session, select
from sqlalchemy import text

from core.env_manager import EnvManager   

DATABASE_URL = EnvManager.get("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL, echo=True)

def get_session() -> Session:
    """
    Return a new SQLModel Session.
    Caller is responsible for closing it when done.
    """
    return Session(engine)


async def check_database_connection():
    """Check if the database connection is working."""
    db = get_session()
    try:
        # Option A: use SQLModel's `exec()` with a SQLModel select()
        result1 = db.exec(select(1))
        print("via select:", result1.one())

        print("Database connected successfully.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    finally:
        db.close()
