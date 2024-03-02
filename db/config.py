import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

load_dotenv()
Base = declarative_base()


class Config:
    DB_USER = 'postgres'
    DB_PASSWORD = '1'
    DB_NAME = 'valyuta_kursi_bot'
    DB_HOST = 'localhost'
    DB_CONFIG = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_NAME = os.getenv("DB_NAME")
# DB_HOST = os.getenv("DB_HOST")

engine = create_engine(Config().DB_CONFIG)
session = Session(engine)
