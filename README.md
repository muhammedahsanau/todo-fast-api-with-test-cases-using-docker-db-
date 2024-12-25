<<<<<<< HEAD
# FastAPI Todo Application with Docker Integration Tests

Overview: This project demonstrates a full-stack FastAPI application for managing a todo list. The application uses PostgreSQL as the database and integrates with Docker for running the database and executing test cases in a containerized environment.

## Features

- FastAPI Backend: Exposes API endpoints to manage todos.
- PostgreSQL Database: Stores todo items and their statuses.
- Docker Integration: Docker Compose is used to run the PostgreSQL database and execute test cases.
- Testing: Integration tests are executed using pytest with a separate test database running in a Docker container.
- Environment Configuration: Uses .env for regular configurations and tests/test.env for the test database.

## Project Structure

```bash
=======
**FastAPI Todo Application with Docker Integration Tests**
*Overview*
This project demonstrates a full-stack FastAPI application for managing a todo list. The application uses PostgreSQL as the database and integrates with Docker for running the database and executing test cases in a containerized environment.

*Features*
FastAPI Backend: Exposes API endpoints to manage todos.
PostgreSQL Database: Stores todo items and their statuses.
Docker Integration: Docker Compose is used to run the PostgreSQL database and execute test cases.
Testing: Integration tests are executed using pytest with a separate test database running in a Docker container.
Environment Configuration: Uses .env for regular configurations and tests/test.env for the test database.
Project Structure
graphql
Copy code
>>>>>>> b32bf48ca7bbfefd7698a66aeea74809aa69e8ff
app/
├── __init__.py
├── main.py               # FastAPI app entry point
├── config.py             # Configuration settings, loads from .env and test.env
├── database.py           # Database connection and session management
├── todo/                 # Todo feature folder
│   ├── __init__.py
│   ├── models.py         # SQLAlchemy models for todos
│   ├── schemas.py        # Pydantic schemas for request/response validation
│   ├── router.py         # FastAPI routes for todo operations
│   ├── service.py        # Business logic for todos
├── tests/                # Test folder
│   ├── test_todo_integration.py  # Integration tests for todo endpoints
│   ├── tests_base.py     # Test setup and fixture management
└── .env                  # Regular environment variables for local development
└── tests/test.env        # Environment variables for testing

docker-compose.yml         # Docker Compose file for running PostgreSQL and FastAPI
docker-compose.test.yml    # Docker Compose file for running tests
```

# Setup and Installation

Overview: This project demonstrates a full-stack FastAPI application for managing a todo list. The application uses PostgreSQL as the database and integrates with Docker for running the database and executing test cases in a containerized environment.

- Clone the repository

```bash
git clone <repository_url>
cd <repository_name>
```

- Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Set up environment variables Create a .env file for regular development configuration:

.env (local development):

```bash
DATABASE_URL=postgresql://postgres:password@localhost:5432/my_db
PY_ENV=DEV
```

- Docker Setup (We use Docker Compose to run the PostgreSQL database and the test cases in isolated containers.)

Run Docker Compose to start PostgreSQL:

```bash
docker-compose -f docker-compose.yml up
```

- Running the application
  Once Docker is up, you can run the FastAPI app using Uvicorn:

```bash
uvicorn app.main:app --reload
```

## Running Tests

To run the tests in an isolated environment, use the following Docker Compose command:

```bash
docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit
```

- Running Tests Locally

```bash
pytest
```

- you can you the following vs code lauch.json (optional):

```bash
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "FastAPI Debug",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "app.main:app",
        "--host",
        "127.0.0.1",
        "--port",
        "8000",
        "--reload"
      ],
      "console": "integratedTerminal",
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      },
      "justMyCode": true
    },
    {
      "name": "Pytest Debug",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": [
        "--maxfail=1", // Stops after the first failed test (optional)
        "--disable-warnings" // Disables warnings cluttering output (optional)
      ],
      "console": "integratedTerminal",
      "justMyCode": true,
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    }
  ]
}

```
