#!/bin/bash
# Run FastAPI app for local development
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
