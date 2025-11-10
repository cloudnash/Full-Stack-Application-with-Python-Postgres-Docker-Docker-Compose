# Full-Stack-Application-with-Python-Postgres-Docker-Docker-Compose

# Fullstack DevOps Assignment

## Prereqs
- Docker & Docker Compose installed
- (Optional) node & npm for local frontend dev

## Run locally with Docker Compose
1. Clone repo
2. Copy .env (already present)
3. Run:
   docker compose up --build

This will build 3 services:
- db (Postgres) on port 5432
- backend (FastAPI) on port 8000
- frontend (React via nginx) on port 3000

Open http://localhost:3000 to use the UI.
API docs available at http://localhost:8000/docs (FastAPI automatic swagger).

## Persisted data
Postgres data is stored in docker volume `db_data`.

## Useful commands
- tail backend logs: `docker compose logs -f backend`
- run shell in backend container: `docker compose exec backend /bin/sh`
- run migrations (if using alembic): see `backend/alembic`

## CI
Jenkins Auotmation tool used for pipleline


```
fullstack-devops-assignment/
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ models.py
│  │  ├─ schemas.py
│  │  ├─ crud.py
│  │  ├─ database.py
│  │  └─ config.py
│  ├─ requirements.txt
│  ├─ Dockerfile
│  └─ start.sh
├─ frontend/
│  ├─ package.json
│  ├─ Dockerfile
│  └─ src/
│     ├─ App.js
│     ├─ index.js
│     ├─ api.js
│     ├─ components/
│        ├─ Users.js
│        ├─ Projects.js
│        └─ Tasks.js
├─ docker-compose.yml
├─ .env
├─ README.md
└─ .github/
   └─ workflows/
      └─ ci.yml

```
