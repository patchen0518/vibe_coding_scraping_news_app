from fastapi import FastAPI
import os
from app.models.db import init_db
from app.utils.ingest_pipeline import run_news_ingestion
from app.routes.news import router as news_router
from app.routes.display import router as display_router
from app.routes.web import router as web_router

app = FastAPI()

CACHE_DIR = os.path.join(os.path.dirname(__file__), '../../.cache')
ERROR_LOG_DIR = os.path.join(os.path.dirname(__file__), '../../.error_log')

@app.on_event("startup")
def startup_event():
    """
    Ensure cache and error log directories exist on startup. Initialize DB and ingest news.
    """
    os.makedirs(CACHE_DIR, exist_ok=True)
    os.makedirs(ERROR_LOG_DIR, exist_ok=True)
    init_db()
    run_news_ingestion()

@app.get("/")
def root():
    """
    Root endpoint for health check.

    Returns:
        dict: Status message.
    """
    return {"status": "News Scraper API is running."}

app.include_router(news_router)
app.include_router(display_router)
app.include_router(web_router)
