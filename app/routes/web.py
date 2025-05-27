"""
FastAPI route to serve the web UI (HTML page) for displaying news.
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from app.models.db import SessionLocal
from app.models.news_article import NewsArticle
from app.utils.news_utils import GENRE_MAP
from collections import defaultdict

router = APIRouter()

TEMPLATES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../templates'))
templates = Jinja2Templates(directory=TEMPLATES_DIR)

@router.get("/", response_class=HTMLResponse)
def serve_home(request: Request):
    """
    Serve the main news display page (all categories, dynamic JS).
    """
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../news_design.html'))
    with open(html_path, "r") as f:
        html = f.read()
    return HTMLResponse(content=html)

@router.get("/category/{category}", response_class=HTMLResponse)
def serve_category(request: Request, category: str):
    """
    Serve a page showing news filtered by normalized_genre (category).
    """
    session = SessionLocal()
    articles = session.query(NewsArticle).filter(NewsArticle.normalized_genre == category).all()
    session.close()
    categories = sorted(set(GENRE_MAP.values()))
    return templates.TemplateResponse(
        "category.html",
        {"request": request, "category": category, "articles": articles, "categories": categories}
    )
