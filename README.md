## Basic FastAPI CRUD implementation

CRUD operations supported API designed using FastAPI

With **Postgres** as database the API is designed to perform CRUD operation to car schema.

To run install the packages and start server

`pip install -r requirements.txt`

`uvicorn app.main:app`

## Summary of Packages

- fastapi: The web framework for building the API.
- pydantic: For data validation and settings management.
- uvicorn: ASGI server to run the FastAPI application.
- sqlalchemy: ORM to interface with the PostgreSQL database.
- asyncpg: Async PostgreSQL driver for higher performance.
- psycopg2: PostgreSQL adapter for Python.
- python-dotenv: To manage environment variables from a .env file.
