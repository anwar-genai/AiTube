# AITube Monorepo

A minimal, working boilerplate for tracking AI-related YouTube channels, transcribing/summarizing new videos, and surfacing results in a simple dashboard.

## Purpose
- Track channels and new uploads via YouTube API.
- Use captions if available; otherwise transcribe audio (Whisper).
- Produce multi-step summaries (LangChain + LangGraph) with hashtags/keywords.
- Store results in Postgres and show them in a Next.js dashboard.

## Features
- Frontend (Next.js App Router + Tailwind)
  - Landing page, pricing page, dashboard (fetches summaries from backend)
  - Simple auth placeholder page (stub)
- Backend (FastAPI)
  - REST APIs: `/channels`, `/videos`, `/summaries`
  - SQLAlchemy models: `User`, `Channel`, `Video`, `Summary`
  - Service stubs for YouTube and Vector DB
  - Agents stubs and sample LangGraph flow
- Workers (Celery)
  - `transcription.py`: Whisper stub
  - `summarization.py`: multi-step summarization stub
  - `publishing.py`: save + notify stub
- Infra (Docker Compose)
  - Services: `frontend`, `backend`, `worker`, `postgres`, `redis`

## Project Structure
```
frontend/   # Next.js (App Router) + Tailwind
backend/    # FastAPI app, models, routers, agents
workers/    # Celery app + tasks (transcription/summarization/publishing)
infra/      # docker-compose.yml
scripts/    # DB init/seed scripts
docs/       # additional docs (optional)
```

## Environment Variables
Create a `.env` in the repo root (same folder as `infra/` and `backend/`).

Notes on quoting:
- Values do not need quotes unless they contain spaces or special characters (e.g., `#`, `=`, `:` with spaces).
- If you quote, `'single'` or "double" quotes both work in a `.env` file.
- In Docker Compose environment files, escape `$` as `$$` if you need a literal dollar sign.

Suggested variables:
```env
# Core APIs
OPENAI_API_KEY=
YOUTUBE_API_KEY=
PINECONE_API_KEY=

# Database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=aitube
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_URI="postgresql+psycopg2://postgres:postgres@postgres:5432/aitube"

# Redis / Celery
REDIS_URL=redis://redis:6379/0

# Backend
SECRET_KEY=changeme
ENV=development

# Frontend
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
```

---

## Getting Started (Docker - Recommended)
Prerequisites: Docker Desktop

```bash
cd infra
# Builds images and installs all deps inside containers
docker compose up --build
```
- Frontend: http://localhost:3000
- Backend health: http://localhost:8000/health

Initialize DB tables (optional) from host:
```bash
python scripts/init_db.py
python scripts/seed.py
```

## Local Development (without Docker)
Prerequisites:
- Node.js 20+
- Python 3.11+
- Postgres 15+, Redis 7+ (you can still run these via Docker)

Run Postgres + Redis with Docker:
```bash
cd infra
docker compose up postgres redis
```

Backend (FastAPI):
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Workers (Celery):
```powershell
cd workers
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
celery -A app.celery_app worker --loglevel=INFO
```

Frontend (Next.js):
```bash
cd frontend
npm install
npm run dev
```

## API Overview
- `POST /channels/` add channel
- `DELETE /channels/{id}` remove channel
- `GET /videos/` list tracked videos
- `GET /summaries/` list summaries

## Next Steps
- Replace service stubs with real YouTube Data API and captions fetching
- Integrate Whisper (local or API) in `workers/app/tasks/transcription.py`
- Implement LangGraph pipeline in `backend/app/agents/sample_graph.py`
- Add Vector DB integration (Pinecone/Weaviate) in `backend/app/vector_store.py`
- Swap auth stub with a real provider (e.g., Clerk/Auth0)

## Troubleshooting
- Ensure `.env` is present at the repo root; Docker Compose uses it and services read it via `env_file`.
- If port conflicts occur, change published ports in `infra/docker-compose.yml`.
- On Windows PowerShell, use `Set-ExecutionPolicy RemoteSigned` if virtualenv activation is blocked.
