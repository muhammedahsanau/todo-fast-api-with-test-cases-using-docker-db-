FastAPI Todo Application with Docker Integration Tests
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
Setup and Installation
*1. Clone the repository*
bash
Copy code
git clone <repository_url>
cd <repository_name>
2. Create a virtual environment (optional but recommended)
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
Make sure the following dependencies are included in requirements.txt:

Copy code
fastapi
uvicorn
sqlalchemy
psycopg2
pytest
pytest-docker
pydantic-settings
4. Set up environment variables
Create a .env file for regular development configuration:

.env (local development):

dotenv
Copy code
DATABASE_URL=postgresql://postgres:password@localhost:5432/my_db
PY_ENV=DEV
Create a tests/test.env file for the testing environment configuration:

tests/test.env (testing environment):

dotenv
Copy code
DATABASE_URL=postgresql://postgres:password@localhost:5433/test_db
PY_ENV=TEST
5. Docker Setup
We use Docker Compose to run the PostgreSQL database and the test cases in isolated containers.

docker-compose.yml: Used for local development to run PostgreSQL and FastAPI together.
docker-compose.test.yml: Used to run tests with a PostgreSQL container for isolated testing.
Run Docker Compose to start PostgreSQL:

bash
Copy code
docker-compose -f docker-compose.yml up
6. Running the application
Once Docker is up, you can run the FastAPI app using Uvicorn:

bash
Copy code
uvicorn app.main:app --reload
Access the FastAPI app at http://127.0.0.1:8000.

Running Tests
1. Integration Tests
To run the tests in an isolated environment, use the following Docker Compose command:

bash
Copy code
docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit
This command will:

Start the PostgreSQL container for testing.
Build and run the FastAPI container.
Execute the tests defined in the tests/test_todo_integration.py file.
2. Test Configuration
The tests_base.py file contains the necessary setup for testing, including:

Database engine setup with SQLAlchemy.
Dependency override to use a test database.
TestClient instance for API calls.
Test database creation and cleanup.
The tests will only run if the environment variable PY_ENV is set to TEST. If it's not, the following error message will be displayed:

bash
Copy code
Cannot run tests if env is not TEST
3. Running Tests Locally
You can also run the tests locally without Docker using pytest:

bash
Copy code
pytest
4. Test Files
tests/test_todo_integration.py: Contains feature-specific tests for the todo API.
tests/tests_base.py: Contains the setup for the test database, TestClient, and other necessary configurations.
