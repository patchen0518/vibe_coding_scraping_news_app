"""
SQLAlchemy models for news articles.
"""
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NewsArticle(Base):
    """
    News article database model.

    Attributes:
        id (int): Unique identifier for the database record.
        article_url (str): The unique URL of the article (used for deduplication).
        title (str): The main title of the news article.
        source_name (str): Name of the news source (e.g., "CNN", "NPR", "BBC News", "NBC News").
        publication_datetime (str): Publication date & time of the article (ISO 8601 format).
        scraped_datetime (str): Timestamp when the article was scraped (ISO 8601 format).
        original_genre (str): Genre as extracted directly from the source website.
        normalized_genre (str): Common genre after applying mapping rules.
        json_cache_filename (str): Filename of the JSON file in the `.cache` directory storing the full article.
    """
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    article_url = Column(Text, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    source_name = Column(String, nullable=False)
    publication_datetime = Column(String, nullable=False)
    scraped_datetime = Column(String, nullable=False)
    original_genre = Column(String)
    normalized_genre = Column(String)
    json_cache_filename = Column(String, nullable=False)
