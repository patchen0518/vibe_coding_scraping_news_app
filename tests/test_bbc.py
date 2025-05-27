"""
Unit tests for BBCScraper.fetch_articles.
"""
import pytest
from unittest.mock import patch, MagicMock
from app.scraper.bbc import BBCScraper

@pytest.fixture
def bbc_scraper():
    return BBCScraper()

@patch("app.scraper.bbc.requests.get")
@patch("app.scraper.bbc.is_today", return_value=True)
@patch("app.scraper.bbc.normalize_genre", side_effect=lambda x: x)
def test_fetch_articles_expected(mock_norm, mock_today, mock_get, bbc_scraper):
    """
    Test fetch_articles returns articles for valid HTML.
    """
    html = '''
    <html><body>
        <a data-testid="external-anchor" href="/news/1" data-bbc-container="World">
            <h2 data-testid="card-headline">Test Headline</h2>
        </a>
    </body></html>
    '''
    mock_resp = MagicMock()
    mock_resp.text = html
    mock_resp.raise_for_status = MagicMock()
    mock_get.return_value = mock_resp

    articles = bbc_scraper.fetch_articles()
    assert len(articles) == 1
    assert articles[0]["title"] == "Test Headline"
    assert articles[0]["article_url"].endswith("/news/1")
    assert articles[0]["original_genre"] == "World"

@patch("app.scraper.bbc.requests.get")
@patch("app.scraper.bbc.is_today", return_value=True)
@patch("app.scraper.bbc.normalize_genre", side_effect=lambda x: x)
def test_fetch_articles_no_articles(mock_norm, mock_today, mock_get, bbc_scraper):
    """
    Test fetch_articles returns empty list if no articles found.
    """
    html = "<html><body></body></html>"
    mock_resp = MagicMock()
    mock_resp.text = html
    mock_resp.raise_for_status = MagicMock()
    mock_get.return_value = mock_resp

    articles = bbc_scraper.fetch_articles()
    assert articles == []

@patch("app.scraper.bbc.requests.get", side_effect=Exception("Network error"))
@patch("app.scraper.bbc.log_scraper_error")
def test_fetch_articles_network_error(mock_log, mock_get, bbc_scraper):
    """
    Test fetch_articles handles network errors gracefully.
    """
    articles = bbc_scraper.fetch_articles()
    assert articles == []
    mock_log.assert_called_once()
