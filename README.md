# Full-Stack-Application-with-Python-Postgres-Docker-Docker-Compose
 
Full Stack DevOps Application

This project is a simple **Full Stack CRUD App** using:
- **FastAPI** backend - – RESTful CRUD APIs for Users, Projects, and Tasks
- **Postgres** database - Persistent local data storage
- **Streamlit** frontend - Simple UI to create and view joined data 
- **Docker Compose** for container orchestration - Each service (backend, frontend, database) runs in its own container 
- **Jenkins** for CI/CD automation (triggered by GitHub webhook) //OPTIONAL BONUS

## Architecture

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

## Prereqs
- Docker & Docker Compose installed
- (Optional) node & npm for local frontend dev

## Run locally with Docker Compose
1. Clone repo
2. Copy .env (already present)
3. Run:
   docker compose up --build
   
```
git clone https://github.com/cloudnash/Full-Stack-Application-with-Python-Postgres-Docker-Docker-Compose.git
cd fullstack-devops-app
docker-compose up -d
```


This will build 3 services:
- db (Postgres) on port 5432
- backend (FastAPI) on port 8000
- frontend (React via nginx) on port 3000

Open http://localhost:3000 to use the UI.
API docs available at http://localhost:8000/docs (FastAPI automatic swagger).

*Images of webpage also added in Image directory.*

## Useful commands
- tail backend logs: `docker compose logs -f backend`
- run shell in backend container: `docker compose exec backend /bin/sh`
- run migrations (if using alembic): see `backend/alembic`


## CI/CD (Bonus: Jenkins Integration)

The task didn’t explicitly ask for automation,
but since this is a DevOps role, I added a Jenkins pipeline that automatically builds and deploys all containers on every code push.
It demonstrates end-to-end CI/CD integration using Jenkins.

-Trigger: Webhook from GitHub → Jenkins
-Pipeline Steps:
-Checkout repository
-Build Docker images
-Run Docker Compose to deploy the stack
-Jenkinsfile is included for reference and can be easily adapted for production or cloud deployment.

### Tech Stack
| Layer | Technology |
|-------|-------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | PostgreSQL |
| *optional* CI/CD | Jenkins |
| Orchestration | Docker Compose |


##Key Takeaways

Clean modular Python backend with RESTful APIs
Persistent Postgres DB
Multi-container orchestration with Docker Compose
Optional CI/CD integration for DevOps demonstration


## Author

Nashit Ahmad

DevOps | Cloud | AWS

📧 nashitakerfeldt@gamil.com

🌐 https://in.linkedin.com/in/nashitahmad
