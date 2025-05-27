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
        seen_urls = set()
        try:
            resp = requests.get(self.BASE_URL, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")

            css_selectors = 'a[data-testid="external-anchor"], a[data-testid="internal-link"]'
            for item in soup.select(css_selectors):
                article_url = item["href"]
                if not article_url.startswith("http"):
                    article_url = f"https://www.bbc.com{article_url}"
                if article_url in seen_urls:
                    continue  # Skip duplicate URLs
                seen_urls.add(article_url)
                # Try to get the title from h1, h2, or h3 inside the link, fallback to link text
                title_tag = None
                for tag in ["h1", "h2", "h3"]:
                    title_tag = item.find(tag, attrs={'data-testid': 'card-headline'})
                    if title_tag and title_tag.get_text(strip=True):
                        break
                if title_tag:
                    title = title_tag.get_text(strip=True)
                else:
                    title = item.get_text(strip=True)
                genre = item.get("data-bbc-container", "News")
                pub_date = datetime.now().isoformat() + "Z"
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
