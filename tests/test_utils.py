import pytest
from app.utils.news_utils import normalize_genre, is_today
from datetime import datetime, timedelta

def test_normalize_genre():
    assert normalize_genre("World News") == "World"
    assert normalize_genre("Tech") == "Tech"
    assert normalize_genre("UnknownGenre") == "UnknownGenre"

def test_is_today_true():
    today = datetime.utcnow().isoformat() + "Z"
    assert is_today(today)

def test_is_today_false():
    yesterday = (datetime.utcnow() - timedelta(days=1)).isoformat() + "Z"
    assert not is_today(yesterday)
