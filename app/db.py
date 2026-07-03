import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


ROOT_PATH = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_PATH / ".env")


def get_database_url() -> str:
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    name = os.getenv("DB_NAME", "octagon_db")
    user = os.getenv("DB_USER", "octagon")
    password = os.getenv("DB_PASSWORD", "12345")

    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"


Base = declarative_base()

engine = create_engine(
    get_database_url(),
    echo=False,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def create_tables() -> None:
    from app import models

    Base.metadata.create_all(bind=engine)
