"""
FastAPI route to serve the web UI (HTML page) for displaying news.
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import os

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def serve_home(request: Request):
    """
    Serve the main news display page (based on news_design.html).
    """
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../news_design.html'))
    with open(html_path, "r") as f:
        html = f.read()
    return HTMLResponse(content=html)
