# 🚀 Drone Management System (Backend)

A production-ready backend system for managing drones, missions, survey areas, and flight paths with role-based access control.

Built using FastAPI, SQLAlchemy, PostgreSQL, and JWT authentication, with a clean layered architecture (Repository → Service → Router).

# 🧱 Tech Stack

- Python 3.11+

- FastAPI

- SQLAlchemy (ORM)

- PostgreSQL

- Alembic (database migrations)

- JWT Authentication

- uv (dependency & environment manager)

- Railway (deployment)

# 📂 Project Structure
- 
    ├── alembic/
    ├── src/
    │   ├── core/            # config, security, jwt
    │   ├── db/              # db session
    │   ├── models/          # SQLAlchemy models
    │   ├── repository/      # DB access layer
    │   ├── services/        # business logic
    │   ├── routers/         # API routes
    │   ├── schemas/         # Pydantic schemas
    │   ├── utils/           # dependencies, helpers
    │   ├── constants/       # error & message constants
    │   ├── enums/           # enums (roles, status, patterns)
    │   └── exceptions/      # custom exceptions & handlers
    ├── main.py
    ├── alembic.ini
    ├── pyproject.toml
    ├── uv.lock
    ├── .env.example
    └── README.md


# 🔐 Authentication & Roles

JWT based authentication

- Roles:

ADMIN

OPERATOR

VIEWER

- Access Control

Admin 

Create drones

Create survey areas

Create operators



Operator

Create missions

Create flight paths


Viewer

Read-only access

# ⚙️ Environment Variables
Local Development

Create a .env file (do not commit it):

POSTGRES_USER=postgres
POSTGRES_PASSWORD=root
POSTGRES_DB=dronedb
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

JWT_SECRET=supersecretkey
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


A template is provided in .env.example.

# 📦 Installation (using uv)
- 1️⃣ Clone the repository
git clone https://github.com/your-username/drone-management-system.git
cd drone-management-system

- 2️⃣ Create virtual environment & install deps
uv sync

- 🗄️ Database Setup
Run migrations
uv run alembic upgrade head

- ▶️ Run the Application
uv run uvicorn main:app --reload


API will be available at:

http://localhost:8000


Swagger UI:

http://localhost:8000/docs

# ☁️ Deployment (Railway)
Steps:

Push code to GitHub (without .env)

Create a new Railway project

Add PostgreSQL plugin

Go to Variables and add:

Database credentials

JWT secrets

Set start command:

uv run uvicorn main:app --host 0.0.0.0 --port $PORT


Railway automatically injects environment variables at runtime.
https://drone-management-system-production-56b6.up.railway.app/


# 🎥 Explanation Video (Assignment) 

In the video, explain: https://drive.google.com/file/d/1l0Gbv2b0Lts89jk6wiCbFOX97XBz3znd/view?usp=sharing

Overall architecture

Role-based access control

JWT authentication flow

Repository vs Service vs Router separation

How missions, drones, and flight paths are linked

Deployment approach on Railway

# ✅ Features Implemented

User authentication & authorization

Role-based access control

Drone management

Survey area management

Mission planning

Flight path generation

Pagination & filtering

Global error handling

Production-ready configuration

# 🧠 Design Decisions

- uv for faster dependency management

- Repository pattern for clean DB abstraction

- Service layer for business logic

- No .env in Git for security

- Enums & constants for consistency

- JWT stateless auth for scalability

# 📌 Notes

Frontend can be added later (Streamlit / React)

System is designed for easy extension (reports, analytics)

