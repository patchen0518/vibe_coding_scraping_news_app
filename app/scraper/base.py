"""
Base class for news scrapers.
"""
from typing import List, Dict, Any
from datetime import datetime

class BaseNewsScraper:
    """
    Abstract base class for news scrapers.
    """
    source_name: str = ""

    def fetch_articles(self) -> List[Dict[str, Any]]:
        """
        Fetch today's articles from the news source.

        Returns:
            List[Dict[str, Any]]: List of article dicts with required fields.
        """
        raise NotImplementedError

    def get_publication_datetime(self, article: Dict[str, Any]) -> str:
        """
        Extract publication datetime in ISO 8601 format from article.
        """
        raise NotImplementedError
