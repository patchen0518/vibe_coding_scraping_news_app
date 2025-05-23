"""
FastAPI route to manually re-fetch news (append new articles only).
"""
from fastapi import APIRouter
from app.utils.ingest_pipeline import run_news_ingestion

router = APIRouter()

@router.post("/refetch-news")
def refetch_news():
    """
    Manually trigger news re-fetch. Appends new articles only.

    Returns:
        dict: Number of new articles ingested.
    """
    count = run_news_ingestion()
    return {"new_articles": count}
