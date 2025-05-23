"""
FastAPI route to serve news articles grouped by category for the web UI.
"""
from fastapi import APIRouter
from app.models.db import SessionLocal
from app.models.news_article import NewsArticle
from collections import defaultdict
from typing import Dict, List

router = APIRouter()

@router.get("/news-by-category")
def get_news_by_category() -> Dict[str, List[dict]]:
    """
    Get all news articles grouped by normalized genre (category).

    Returns:
        dict: {category: [articles]}
    """
    session = SessionLocal()
    articles = session.query(NewsArticle).all()
    session.close()
    grouped = defaultdict(list)
    for a in articles:
        grouped[a.normalized_genre or "Other"].append({
            "title": a.title,
            "url": a.article_url,
            "source": a.source_name,
            "publication_datetime": a.publication_datetime,
        })
    return grouped
