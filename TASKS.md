# Scarping News App

## Project Setup
- [x] Project structure scaffolded (app, models, scraper, routes, utils, tests)
- [x] requirements.txt, Dockerfile, .env.example, start.sh created
- [x] Database schema and models implemented
- [x] Ingestion pipeline implemented and triggered on startup
- [x] Scraper base and all four source scrapers stubbed
- [x] API endpoints for health, refetch, news-by-category, and web UI
- [x] Initial tests for API and utils
- [x] Error logging utility
- [x] All code follows PEP8, type hints, and docstring conventions

## Discovered During Work
- [ ] Improve per-source publication date extraction (currently uses fallback)
- [ ] Add more robust genre mapping and error handling for edge cases
- [ ] Add UI logic to fetch/display news from /news-by-category

## Testing
- [ ] Create unit tests for document processing
- [ ] Create unit tests for knowledge base search
- [ ] Create unit tests for agent functionality

## Documentation
- [ ] Update README.md with setup and usage instructions

## Discovered During Work
- [ ] Add support for more document types (e.g., DOCX, HTML)
- [ ] Implement metadata filtering in the UI
- [ ] Add visualization of vector embeddings
- [ ] Create a CLI interface for batch document processing