import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    resp = client.get("/")
    assert resp.status_code == 200
    assert "News Scraper API" in resp.text or "DOCTYPE html" in resp.text

def test_refetch_news():
    resp = client.post("/refetch-news")
    assert resp.status_code == 200
    assert "new_articles" in resp.json()

def test_news_by_category():
    resp = client.get("/news-by-category")
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)
