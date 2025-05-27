"""
CNN news scraper implementation.
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List, Dict, Any
from app.scraper.base import BaseNewsScraper
from app.utils.news_utils import normalize_genre, is_today

class CNNScraper(BaseNewsScraper):
    source_name = "CNN"
    BASE_URL = "https://edition.cnn.com/"

    def fetch_articles(self) -> List[Dict[str, Any]]:
        """
        Fetch today's articles from CNN World page.
        """
        articles = []
        seen_urls = set()
        try:
            resp = requests.get(self.BASE_URL, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")

            css_selectors = 'a[class="container__link container__link--type-article container_lead-plus-headlines__link container_lead-plus-headlines__left container_lead-plus-headlines__light"]'
            for item in soup.select(css_selectors):
                link = item.find("a", href=True)
                if not link:
                    continue
                article_url = link["href"]
                if not article_url.startswith("http"):
                    article_url = f"https://edition.cnn.com{article_url}"
                if article_url in seen_urls:
                    continue  # Skip duplicate URLs
                seen_urls.add(article_url)
                # Try to get the title from h1, h2, or h3 inside the link, fallback to link text
                title_tag = None
                for tag in ["h1", "h2", "h3"]:
                    title_tag = item.find(tag, attrs={'data-editable="title"'})
                    if title_tag and title_tag.get_text(strip=True):
                        break
                if title_tag:
                    title = title_tag.get_text(strip=True)
                else:
                    title = link.get_text(strip=True)
                # CNN genre extraction is not always present; fallback to 'World'
                genre = item.get("data-section-name", "World")
                # Publication date extraction (CNN markup varies, so fallback to now)
                pub_date = datetime.now().isoformat() + "Z"
                # Reason: CNN's homepage often lacks explicit pub date; fallback to now
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
            # Reason: Log error for debugging and reliability
            from app.utils.error_utils import log_scraper_error
            log_scraper_error(self.source_name, str(e))
        return articles
