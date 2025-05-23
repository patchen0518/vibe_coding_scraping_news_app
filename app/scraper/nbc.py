"""
NBC News scraper implementation.
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List, Dict, Any
from app.scraper.base import BaseNewsScraper
from app.utils.news_utils import normalize_genre, is_today
from app.utils.error_utils import log_scraper_error

class NBCScraper(BaseNewsScraper):
    source_name = "NBC News"
    BASE_URL = "https://www.nbcnews.com/news"

    def fetch_articles(self) -> List[Dict[str, Any]]:
        articles = []
        try:
            resp = requests.get(self.BASE_URL, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            for item in soup.select("article"):
                link = item.find("a", href=True)
                if not link:
                    continue
                article_url = link["href"]
                if not article_url.startswith("http"):
                    article_url = f"https://www.nbcnews.com{article_url}"
                title = link.get_text(strip=True)
                genre = item.get("data-vertical", "News")
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
