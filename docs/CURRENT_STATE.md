# Current State

## Status

AI Career Agent foundation is complete. The application can accept, validate, and return structured job and candidate profile data through FastAPI.

Both APIs currently use simulated IDs. No data is persisted.

## What Works

### Project Foundation
- Python 3.12 and dependencies managed with `uv`
- FastAPI application running locally
- `GET /health` returns `{"status": "ok"}`
- OpenAPI/Swagger documentation available at `/docs`
- Git repository initialized with `main` branch
- Private GitHub repository configured using SSH

### Job API
- `JobCreate` defines the API input contract
- `JobResponse` extends `JobCreate` with an ID
- `POST /jobs` accepts and validates structured job data
- Returns HTTP 201 with a simulated `id=1`
- Supports job details including compensation, location, work arrangement, travel, and description

### Candidate Profile API
- `CandidateProfileCreate` defines candidate information:
  - Name, headline, summary, skills, target roles, location
- Nested `CandidatePreferences` model:
  - Minimum salary
  - Preferred work arrangement
  - Maximum travel percentage
- `CandidateProfileResponse` extends `CandidateProfileCreate` with an ID
- `POST /candidates` accepts and validates candidate profiles
- Returns HTTP 201 with a simulated `id=1`

### Automated Tests
- pytest with FastAPI `TestClient`
- **5 passing tests:**
  - Successful job creation
  - Missing required job title
  - Invalid job travel percentage type
  - Successful candidate creation with nested preferences
  - Missing required candidate name
- One non-blocking FastAPI/Starlette dependency warning

## Current Structure

- `src/ai_career_agent/` — application source
- `src/ai_career_agent/schemas/` — Pydantic models
- `tests/` — automated tests
- `docs/` — project documentation
- `docs/adr/` — architecture decision records

## Not Implemented Yet

- Database/persistence
- Job and candidate retrieval endpoints
- LLM integration
- Job-fit evaluation
- Application tracking
- Duplicate detection
- Agent/tool calling
- RAG
- Cloud deployment

## Next Milestone

**PostgreSQL persistence**

Persist jobs and candidate profiles instead of returning simulated IDs.

Introduce SQLAlchemy for database access and Alembic for schema migrations.
