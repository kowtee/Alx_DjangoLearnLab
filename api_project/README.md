# api_project – Django REST Framework API

This project is part of the **“Introduction to Building APIs with Django REST Framework”** track.  
It demonstrates how to build a basic RESTful API using Django and Django REST Framework (DRF).

## Features

- Django project: `api_project`
- App: `api`
- Model: `Book` with fields:
  - `title` (CharField)
  - `author` (CharField)
- DRF used for:
  - Serializers
  - ViewSets
  - Routers
  - Authentication & Permissions

## API Endpoints

All endpoints are prefixed with `/api/`.

- `GET /api/books/`  
  List all books.

- `POST /api/books/`  
  Create a new book (authenticated users only).

- `GET /api/books/<id>/`  
  Retrieve a single book.

- `PUT /api/books/<id>/`  
  Update a book completely.

- `PATCH /api/books/<id>/`  
  Partially update a book.

- `DELETE /api/books/<id>/`  
  Delete a book (authenticated users only).

## Authentication & Permissions

Django REST Framework settings:

- Uses `SessionAuthentication` and `BasicAuthentication`.
- Default permission: `IsAuthenticatedOrReadOnly`.

This means:

- Anyone can **read** data (`GET` requests).
- Only logged-in users can **create, update, or delete** (`POST`, `PUT`, `PATCH`, `DELETE`).

Login is handled via DRF’s browsable API:

- `/api-auth/login/`
- `/api-auth/logout/`

## How to Run the Project

1. Activate the virtual environment:

   ```bash
   cd /Users/user/GitHubCloneProject/Alx_DjangoLearnLab/Alx_DjangoLearnLab
   source .venv/bin/activate

