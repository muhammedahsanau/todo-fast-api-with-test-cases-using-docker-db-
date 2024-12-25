from app.tests.tests_base import client  # Import TestClient from tests_base.py

def test_create_todo():
    response = client.post("/todos/", json={"title": "Test Todo", "description": "Test Desc", "is_completed": False})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Todo"

def test_get_todo():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_todo_2():
    response = client.post("/todos/", json={"title": "Test Todo", "description": "Test Desc", "is_completed": False})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Todo"

def test_get_todo_2():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert len(response.json()) > 0
