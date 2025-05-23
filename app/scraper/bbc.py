"""
BBC News scraper implementation.
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List, Dict, Any
from app.scraper.base import BaseNewsScraper
from app.utils.news_utils import normalize_genre, is_today
from app.utils.error_utils import log_scraper_error

class BBCScraper(BaseNewsScraper):
    source_name = "BBC News"
    BASE_URL = "https://www.bbc.com/news"

    def fetch_articles(self) -> List[Dict[str, Any]]:
        articles = []
        try:
            resp = requests.get(self.BASE_URL, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            for item in soup.select("a.gs-c-promo-heading"):
                article_url = item["href"]
                if not article_url.startswith("http"):
                    article_url = f"https://www.bbc.com{article_url}"
                title = item.get_text(strip=True)
                genre = item.get("data-bbc-container", "News")
                pub_date = datetime.utcnow().isoformat() + "Z"
                if is_today(pub_date):
                    articles.append({
                        "article_url": article_url,
                        "title": title,
                        "source_name": self.source_name,
                        "publication_datetime": pub_date,
                        "original_genre": genre,
                        "normalized_genre": normalize_genre(genre),
                    })
        except Exception as e:
            log_scraper_error(self.source_name, str(e))
        return articles
