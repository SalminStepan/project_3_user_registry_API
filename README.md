# Project 3 — User Registry API (FastAPI + PostgreSQL)

REST API service for managing users using **FastAPI** and **PostgreSQL**.
This project continues the previous CLI version and demonstrates how to build a backend service with:
* REST API
* PostgreSQL storage
* Repository pattern
* Dependency Injection
* Pagination
* Search
* Error handling

# Tech Stack
* Python 3.10+
* FastAPI
* PostgreSQL
* psycopg (v3)
* Pydantic
* Uvicorn

# Project Structure

```
project_3_user_registry_api
│
├── app
│   ├── api.py        # API endpoints
│   ├── repo.py       # database queries (repository layer)
│   ├── schemas.py    # Pydantic models
│   ├── db.py         # repository dependency
│   └── main.py       # FastAPI application
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

### 1. Clone repository

```
git clone <your_repo_url>
cd project_3_user_registry_api
```

---

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

# Database Setup

Create database:

```
createdb user_registry
```

Or in PostgreSQL:

```
CREATE DATABASE user_registry;
```

Apply schema:

```
psql -U stepan -d user_registry -h localhost -f schema.sql
```

---

# Environment Variables

Set database connection string:

```
export USER_REGISTRY_DSN="host=localhost port=5432 dbname=user_registry user=stepan password=YOUR_PASSWORD"
```

---

# Running the API

Start the server:

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# API Documentation

Interactive documentation is available at:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows testing all endpoints directly from the browser.

---

# API Endpoints

### Create user

```
POST /users
```

Body:

```
{
  "name": "Ivan",
  "phone": "+77001231231",
  "city": "Almaty"
}
```

---

### List users

```
GET /users
```

Supports:

```
?search=
?limit=
?offset=
```

Example:

```
GET /users?limit=10&offset=0
```

---

### Get user by ID

```
GET /users/{user_id}
```

---

### Update user

```
PUT /users/{user_id}
```

---

### Delete user

```
DELETE /users/{user_id}
```

---

# Example Requests (CLI)

Get users:

```
curl http://127.0.0.1:8000/users | python3 -m json.tool
```

Search:

```
curl "http://127.0.0.1:8000/users?search=ivan"
```

Create user:

```
curl -X POST http://127.0.0.1:8000/users \
-H "Content-Type: application/json" \
-d '{"name":"Alex","phone":"+79990000003","city":"Berlin"}'
```

---

# Architecture

The application follows a layered architecture.

### API Layer

Handles:

* HTTP requests
* input validation
* response serialization

### Repository Layer

Responsible for:

* database access
* SQL queries
* translating database errors

### Database

PostgreSQL stores user data.

---

# Author

Stepan Salmin
Backend learning project (Python + PostgreSQL)
