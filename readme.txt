FastAPI Todo Application with Docker Integration Tests
Overview
This project demonstrates a full-stack FastAPI application for managing a todo list. The application uses PostgreSQL as the database and integrates with Docker for running the database and executing test cases in a containerized environment.

Features
FastAPI Backend: Exposes API endpoints to manage todos.
PostgreSQL Database: Stores todo items and their statuses.
Docker Integration: Docker Compose is used to run the PostgreSQL database and execute test cases.
Testing: Integration tests are executed using pytest with a separate test database running in a Docker container.
Environment Configuration: Uses .env for regular configurations and tests/test.env for the test database.
