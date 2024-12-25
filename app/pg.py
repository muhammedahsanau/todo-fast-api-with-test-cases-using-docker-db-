import psycopg2
from app.config import settings

def get_db_connection():
    """Establishes and returns a connection to the PostgreSQL database."""
    conn = psycopg2.connect(settings.database_url)
    return conn

def fetch_all_todos():
    """Fetches all todos from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, is_completed, created_at FROM todos")
    todos = cursor.fetchall()
    cursor.close()
    conn.close()
    return todos

def pg_fetch_all_todos_ilike(title):
    """Fetches all todos from the database based on a case-insensitive title search."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, description, is_completed, created_at FROM todos WHERE title ILIKE %s",
        (f"%{title}%",)  # Add wildcards and ensure it's passed as a tuple
    )
    todos = cursor.fetchall()
    cursor.close()
    conn.close()
    return todos


def insert_todo(title, description):
    """Inserts a new todo into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todos (title, description) VALUES (%s, %s) RETURNING id",
        (title, description),
    )
    todo_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return todo_id
