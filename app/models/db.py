"""
Database initialization and session management for the news scraping app.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DATABASE_URL", "sqlite:///./app.db")
engine = create_engine(DB_PATH, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from app.models.news_article import Base

def init_db():
    """
    Initialize the database and create tables if they do not exist.
    """
    Base.metadata.create_all(bind=engine)
