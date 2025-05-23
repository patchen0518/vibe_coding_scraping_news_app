# Vibe Coding Scraping News App

## 1. Summary
This application automatically scrapes daily news articles from selected sources (CNN, NPR, NBC News, BBC), categorizes them by genre, and centralizes them for display in a local web interface. It features automated and manual news fetching, local caching, deduplication, and a simple web UI for browsing categorized news. The app is containerized for easy deployment.

## 2. File Structure
```
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI app entrypoint
│   ├── models/                # Database models & DB init
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── news_article.py
│   ├── routes/                # API and web routes
│   │   ├── __init__.py
│   │   ├── display.py
│   │   ├── news.py
│   │   └── web.py
│   ├── scraper/               # Scraper logic for each source
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── bbc.py
│   │   ├── cnn.py
│   │   ├── nbc.py
│   │   └── npr.py
│   └── utils/                 # Utilities (genre, ingest, error)
│       ├── __init__.py
│       ├── error_utils.py
│       ├── ingest_pipeline.py
│       └── news_utils.py
├── tests/                     # Pytest unit tests
│   ├── __init__.py
│   ├── test_api.py
│   └── test_utils.py
├── .cache/                    # Cached news articles (created at runtime)
├── .error_log/                # Error logs (created at runtime)
├── cache_example.json         # Example of cached article
├── DATABASE_SCHEMA.md         # DB schema reference
├── Dockerfile                 # For containerization
├── news_design.html           # Web UI design template
├── PLANNING.md                # Project planning & rules
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── start.sh                   # Shell script to run app
├── TASKS.md                   # Task tracking
```

## 3. Tech Stack
- **Python 3.11**
- **FastAPI** (web framework)
- **SQLAlchemy** (ORM for SQLite)
- **Requests** & **BeautifulSoup4** (web scraping)
- **Uvicorn** (ASGI server)
- **Pytest** (testing)
- **Docker** (containerization)

## 4. How to Start & Run the App

### Prerequisites
- Python 3.11+
- (Optional) Docker

### Local Development
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the app:**
   ```bash
   ./start.sh
   ```
   Or manually:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
3. **Access the app:**
   - Web UI: [http://localhost:8000](http://localhost:8000)
   - API endpoints:
     - `POST /refetch-news` — Manually fetch new news
     - `GET /news-by-category` — Get news grouped by category

### Using Docker
1. **Build the image:**
   ```bash
   docker build -t news-scraper-app .
   ```
2. **Run the container:**
   ```bash
   docker run -p 8000:8000 news-scraper-app
   ```

### Testing
Run all tests with:
```bash
pytest
```

---
For more details, see `PLANNING.md` and `TASKS.md`.
