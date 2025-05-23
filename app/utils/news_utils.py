"""
Utility functions for genre normalization and date handling.
"""
from datetime import datetime
from typing import Dict

# Example genre mapping (expand as needed)
GENRE_MAP: Dict[str, str] = {
    "World News": "World",
    "Global": "World",
    "Politics": "Politics",
    "US": "US",
    "Business": "Business",
    "Health": "Health",
    "Science": "Science",
    "Technology": "Tech",
    "Tech": "Tech",
    "Sports": "Sports",
    "Entertainment": "Entertainment",
    # Add more as needed
}

def normalize_genre(original_genre: str) -> str:
    """
    Normalize a genre string to a common set.

    Args:
        original_genre (str): Genre as extracted from the source.

    Returns:
        str: Normalized genre.
    """
    return GENRE_MAP.get(original_genre.strip(), original_genre.strip())

def is_today(date_str: str) -> bool:
    """
    Check if the given ISO 8601 date string is today (UTC).

    Args:
        date_str (str): Date string in ISO 8601 format.

    Returns:
        bool: True if date is today, else False.
    """
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.date() == datetime.utcnow().date()
    except Exception:
        return False
