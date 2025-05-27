"""
Utility functions for genre normalization and date handling.
"""
from datetime import datetime
from typing import Dict

# Example genre mapping (expand as needed)
GENRE_MAP: Dict[str, str] = {
    # BBC News
    "Home": "Top Stories",
    "News": "Top Stories",
    "World": "World",
    "US & Canada": "World",
    "UK": "World",
    "Africa": "World",
    "Asia": "World",
    "Australia": "World",
    "Europe": "World",
    "Latin America": "World",
    "Middle East": "World",
    "Business": "Business",
    "Technology": "Technology",
    "Sport": "Sports",
    "Science": "Science",
    "Health": "Science",
    "Climate": "Science",
    "Environment & Nature": "Science",
    # CNN
    "Main page headlines": "Top Stories",
    "US": "Top Stories",
    "Tech": "Technology",
    # NPR News
    "Main news page headlines": "Top Stories",
    "Technology": "Technology",
    "Sports": "Sports",
    # NBC News
    "Main page headlines": "Top Stories",
    "U.S. News": "Top Stories",
    "Tech & Media": "Technology",
    "Sports": "Sports",
    # General
    "Top Stories": "Top Stories",
    "World": "World",
    "Business": "Business",
    "Technology": "Technology",
    "Sports": "Sports",
    "Science": "Science",
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
