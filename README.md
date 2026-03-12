# User Registry API (FastAPI + PostgreSQL)

Simple REST API for managing users.

This project demonstrates a basic backend architecture using:

* FastAPI
* PostgreSQL
* Repository pattern
* Pydantic schemas
* Dependency Injection

The API supports full CRUD operations, search, and pagination.

---

## Project Structure

```
app/
├── core/
│   └── db.py
├── repositories/
│   └── users.py
├── routers/
│   └── users.py
├── schemas/
│   └── users.py
└── main.py
```

---

## Requirements

Python 3.10+

Install dependencies:

```
pip install -r requirements.txt
```

---

## Database

Create database:

```
createdb user_registry
```

Apply schema:

```
psql -U postgres -d user_registry -f schema.sql
```

---

## Environment Variable

The application expects a DSN string in an environment variable.

Example:

```
export USER_REGISTRY_DSN="host=localhost port=5432 dbname=user_registry user=postgres password=yourpassword"
```

---

## Run the API

From project root:

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## Endpoints

### Create user

POST /users

```
{
  "name": "Ivan",
  "phone": "+77001234567",
  "city": "Almaty"
}
```

---

### Get users

GET /users

Query parameters:

```
search
limit
offset
```

---

### Get user by id

GET /users/{id}

---

### Update user

PUT /users/{id}

---

### Partial update

PATCH /users/{id}

---

### Delete user

DELETE /users/{id}

---

## Features

* PostgreSQL storage
* Repository pattern
* Pagination (limit / offset)
* Search by name / phone / city
* Partial updates
* Swagger documentation

---

## Author

Stepan Salmin

Backend learning project (FastAPI + PostgreSQL)

