# Full-Stack-Application-with-Python-Postgres-Docker-Docker-Compose

# Full Stack DevOps Application

This project is a simple **Full Stack CRUD App** using:
- **FastAPI** backend
- **Postgres** database
- **Streamlit** frontend
- **Docker Compose** for container orchestration
- **Jenkins** for CI/CD automation (triggered by GitHub webhook) //OPTIONAL BONUS

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

## Useful commands
- tail backend logs: `docker compose logs -f backend`
- run shell in backend container: `docker compose exec backend /bin/sh`
- run migrations (if using alembic): see `backend/alembic`


## Architecture
![Architecture](docs/architecture-diagram.png)

### Tech Stack
| Layer | Technology |
|-------|-------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | PostgreSQL |
| *optional* CI/CD | Jenkins |
| Orchestration | Docker Compose |

## How to Run

```bash
git clone https://github.com/<your-username>/fullstack-devops-app.git
cd fullstack-devops-app
docker-compose up -d
```


```
📦 fullstack-devops-assignment/
 fullstack-devops-app/
├── backend/
│   ├── Dockerfile
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── crud.py
│   │   ├── schema.py
│   │   └── database.py
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   └── dist/
│       └── index.html   ← this is your frontend
├── docker-compose.yml
├── Jenkinsfile
└── README.md


```
