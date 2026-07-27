from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///news.db"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    #true включает логи
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()