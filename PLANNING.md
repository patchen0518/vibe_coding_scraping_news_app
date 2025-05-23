# Project Planning: Daily news scraping

## Project Overview
Building an app that scrap daily news from selected source and centralized it in a single place.

## Architecture

### Core Component
1. **Scraping daily news from each selected source**
  - Get all today's articles and their content from the following website
   - https://edition.cnn.com
   - https://www.npr.org
   - https://www.nbcnews.com
   - https://www.bbc.com
  - Sort the article based on the genre

2. **Website that display the news**
  - Follow the example format from the file *news_design.html* to create the website.

3. **Daily Saved/Cached content**
  - Saved the scraped news locally, provide the saving path
  - Cleared the cached file during news run if the news date is not today
  - If the news refetch, append the new news and keep the same article without change.


### Technology Stacks:
  - Web Framework: We'll proceed with FastAPI. It's modern, high-performance, and its design should make development straightforward for this project.
  - Database System: SQLite is confirmed. This is a good choice for a local application, requiring no separate database server.
  - Scraping Libraries: We'll use Requests for HTTP calls and Beautiful Soup 4 for HTML parsing.

### Scraping Logic:
  - Genre will be extracted directly from the news websites. A genre normalization step will be implemented to map different source-specific genres to a common set (e.g., "World News" from one source and "Global" from another could both be mapped to a "World" category). You will need to define these mapping rules.
  - "Today's articles" will be identified by their publication date.
  - If a scraper fails due to website structure changes, the system will log the error (see Error Handling below) and cease scraping from that specific source for that run, preventing a full application crash.

### News Storage & Caching:
  - Storage Path: `/Users/<useraccount>/Developer/AI_agent/vibe_coding_scraping_news_app/.cache/` (The .cache folder will be created if it doesn't exist).
  - Format: Scraped articles (including their full content) will be stored as individual JSON files within this directory. (Example file can refer to the *cache_example.json)
  - Deduplication: Existing articles will be identified using their unique `article_url`.

### Error Handling & Logging:
  - Errors (especially scraping errors) will be logged to a file located at `/Users/<useraccount>/Developer/AI_agent/vibe_coding_scraping_news_app/.error_log/` (The .error_log folder will also be created if it doesn't exist).
  - For the "send error notification to the developer" requirement, for now, this will be met by writing detailed logs to this file. If you need more active notifications (e.g., email alerts)

### Application Scope: 
News fetching will be automatically triggered when the FastAPI local web server starts up.

## Development Process

The development will follow a task-based approach where each component will be implemented sequentially. We should:

1. Start by setting up the project structure
2. Create database tables, schema can refer to the *DATABASE_SCHEMA.md* file.
3. Implement simple news ingestion pipeline
4. Develop UI
6. Connect all components and ensure they work together
7. Test the complete system
8. Create Dockerfile and contanized the app

## Design Principles

1. **Modularity**: Keep components decoupled for easier maintenance
2. **Simplicity**: Focus on making the system easy to understand and modify
3. **Performance**: Optimize for response time in knowledge retrieval

## Environment Configuration

Create a `.env.example` file with the following variables (if any):


This file will serve as a template for users to create their own `.env` file.

## Expected Output

A functional where users can:
- Automatically fetch the daily news when app launch.
- Re-fetch news with a click of a button.
- Append the new news during re-fetch. Don't change the existing news.
- Discard the news that does not have today's date.
- Display the collected news in categories.

## Notes

When implementing this project, make sure to:
- Mark tasks complete in the TASKS.md file as you finish them
- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check `TASKS.md`** before starting a new task. If the task isn’t listed, add it with a brief description and today's date.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.

### 🧱 Code Structure & Modularity
- **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
- **Use clear, consistent imports** (prefer relative imports within packages).

### 🧪 Testing & Reliability
- **Always create Pytest unit tests for new features** (functions, classes, routes, etc).
- **After updating any logic**, check whether existing unit tests need to be updated. If so, do it.
- **Tests should live in a `/tests` folder** mirroring the main app structure.
  - Include at least:
    - 1 test for expected use
    - 1 edge case
    - 1 failure case

### ✅ Task Completion
- **Mark completed tasks in `TASKS.md`** immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASKS.md` under a “Discovered During Work” section.

### 📎 Style & Conventions
- **Use Python** as the primary language.
- **Follow PEP8**, use type hints, and format with `black`.
- Write **docstrings for every function** using the Google style:
  ```python
  def example():
      """
      Brief summary.

      Args:
          param1 (type): Description.

      Returns:
          type: Description.
      """
  ```

### 📚 Documentation & Explainability
- **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.

### 🧠 AI Behavior Rules
- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions** – only use known, verified Python packages.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASKS.md`.