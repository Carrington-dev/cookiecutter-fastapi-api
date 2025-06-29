# 🚀 {{ cookiecutter.project_name }}

An **asynchronous FastAPI web API** project scaffold, built with modern best practices:

- ✅ FastAPI with async support
- ✅ JWT Authentication (Register/Login)
- ✅ SQLAlchemy async ORM
- ✅ PostgreSQL or SQLite (via SQLModel or SQLAlchemy 2.0)
- ✅ Alembic migrations
- ✅ Docker-ready
- ✅ Poetry (via `pyproject.toml`)
- ✅ Linting and testing setup

---

## 📦 Project Structure

```bash

{{ cookiecutter.project_slug }}/
├── app/
│   ├── api/             # API routes (v1/users, auth)
│   ├── core/            # Config, security
│   ├── db/              # Database session and base
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   └── main.py          # FastAPI entrypoint
├── tests/               # Unit tests
├── pyproject.toml       # Poetry config
├── Dockerfile           # Container setup
├── .env                 # Env variables
└── README.md

````

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/docs/)
- Docker (optional)

---

### 🧱 Setup Locally

```bash
# Clone the generated repo
cd {{ cookiecutter.project_slug }}

# Install dependencies
poetry install

# Activate shell
poetry shell

# Run the server
uvicorn app.main:app --reload
````

---

### 🧪 Run Tests

```bash
pytest
```

---

### 🔐 Auth Endpoints

* `POST /auth/register` — Create a user
* `POST /auth/login` — Get JWT token
* `GET /auth/me` — Authenticated user info (requires token)

---

### ⚙️ Env Configuration

Create a `.env` file like:

```env
DATABASE_URL=sqlite+aiosqlite:///./dev.db
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🐳 Run with Docker

```bash
docker build -t {{ cookiecutter.project_slug }} .
docker run -p 8000:8000 {{ cookiecutter.project_slug }}
```

---

## 📜 Migrations (with Alembic)

```bash
# Run migrations
alembic upgrade head

# Create new migration
alembic revision --autogenerate -m "Add users table"
```

---

## ✅ Features

* 🔐 Secure password hashing (bcrypt)
* 🧠 Async database operations
* 🧪 Typed request/response validation with Pydantic
* 🧱 Modular, scalable architecture
* ⚙️ Configured for production with Gunicorn/Uvicorn and Docker

---

## ✨ Credits

Created with 💡 by \[{{ cookiecutter.author\_name }}].

---

## 📄 License

This project is licensed under the MIT License.

```bash
Perfect! Here's what I’ll do for you:
```
---

## ✅ Action Plan

I’ll prepare and deliver:

1. **Fully working Cookiecutter template** for:

   * FastAPI (async)
   * User registration/login with JWT
   * SQLAlchemy async
   * Docker support
   * Poetry with `pyproject.toml`
   * Alembic migrations
   * Optional PostgreSQL/SQLite support

2. **GitHub-ready structure** so you can use it with:

```bash
cookiecutter gh:CarringtonMuleya/cookiecutter-fastapi-api
```

3. A `.zip` version you can download and use offline.

---

## 📦 Your Template Name (suggested)

`cookiecutter-fastapi-api`

---
## Generate Secret Key

### 🔐 Option 1: Python One-liner (recommended)

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

#### 🔢 Example Output:

```
sKk4GdLU1TtnlqdY9L43ZgoHoJ_pGl0V5IlMoyeqFZs
```

This generates a **256-bit URL-safe** random string.

---

### 🔐 Option 2: From Python REPL

```python
import secrets
secrets.token_urlsafe(32)
```

---

### 🔐 Option 3: Using OpenSSL (Linux/macOS)

```bash
openssl rand -base64 32
```

---

### 📌 How to Use in `.env`

```env
SECRET_KEY=sKk4GdLU1TtnlqdY9L43ZgoHoJ_pGl0V5IlMoyeqFZs
```

Or in code:

```python
import os
SECRET_KEY = os.getenv("SECRET_KEY")
```

---


{% if cookiecutter.use_docker == "yes" %}
## 🐳 Docker

To run the app with Docker:

```bash
docker-compose up --build
```

{% endif %}


---


## 🗄️ Database

This project is configured to use:

{% if cookiecutter.database == "sqlite" %}
- SQLite for local development with `aiosqlite`
{% elif cookiecutter.database == "postgresql" %}
- PostgreSQL via `asyncpg`
{% elif cookiecutter.database == "mysql" %}
- MySQL via `aiomysql`
{% endif %}

The connection string is defined in `.env` under `DATABASE_URL`.






<!-- ## 🔄 Do You Want Any of These?

* ✅ Optional Celery + Redis for background tasks?
* ✅ Role-based access control?
* ✅ GitHub Actions CI?
* ✅ Email verification?
* ✅ Admin dashboard?

Please confirm or specify preferences — I’ll then:

* Generate the template
* Push it to your GitHub
* Send you the zip download link

Let me know your final customization preferences, or just say “proceed with defaults.” -->
