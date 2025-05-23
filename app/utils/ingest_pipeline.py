"""
Pipeline to run all scrapers, deduplicate, and save articles to cache and DB.
"""
from typing import List, Dict, Any
from datetime import datetime
import os
import json
from app.scraper.cnn import CNNScraper
from app.scraper.npr import NPRScraper
from app.scraper.nbc import NBCScraper
from app.scraper.bbc import BBCScraper
from app.models.db import SessionLocal
from app.models.news_article import NewsArticle
from app.utils.news_utils import is_today

CACHE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.cache'))

SCRAPERS = [CNNScraper(), NPRScraper(), NBCScraper(), BBCScraper()]

def run_news_ingestion() -> int:
    """
    Run all scrapers, deduplicate, and save today's news to cache and DB.

    Returns:
        int: Number of new articles ingested.
    """
    os.makedirs(CACHE_DIR, exist_ok=True)
    session = SessionLocal()
    new_count = 0
    for scraper in SCRAPERS:
        articles = scraper.fetch_articles()
        for article in articles:
            if not is_today(article["publication_datetime"]):
                continue
            # Deduplication by article_url
            exists = session.query(NewsArticle).filter_by(article_url=article["article_url"]).first()
            if exists:
                continue
            # Save article JSON to cache
            filename = f"{scraper.source_name.lower()}_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.json"
            filepath = os.path.join(CACHE_DIR, filename)
            with open(filepath, "w") as f:
                json.dump(article, f)
            # Add to DB
            db_article = NewsArticle(
                article_url=article["article_url"],
                title=article["title"],
                source_name=article["source_name"],
                publication_datetime=article["publication_datetime"],
                scraped_datetime=datetime.now().isoformat() + "Z",
                original_genre=article["original_genre"],
                normalized_genre=article["normalized_genre"],
                json_cache_filename=filename,
            )
            session.add(db_article)
            new_count += 1
    session.commit()
    session.close()
    return new_count
