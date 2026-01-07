from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./career_agent.db"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ✅ THIS FUNCTION WAS MISSING
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
