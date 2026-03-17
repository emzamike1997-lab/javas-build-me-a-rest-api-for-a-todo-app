### === test_todo_model.py ===
```python
import unittest
from todo_app.models import Todo

class TestTodoModel(unittest.TestCase):
    def test_todo_creation(self):
        todo = Todo(title="Test Todo", description="This is a test todo")
        self.assertEqual(todo.title, "Test Todo")
        self.assertEqual(todo.description, "This is a test todo")

    def test_todo_str_representation(self):
        todo = Todo(title="Test Todo", description="This is a test todo")
        self.assertEqual(str(todo), "Test Todo")

if __name__ == "__main__":
    unittest.main()
```

### === test_todo_api.py ===
```python
import unittest
import json
from todo_app import app, db
from todo_app.models import Todo

class TestTodoAPI(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        db.create_all()

    def test_get_all_todos(self):
        todo1 = Todo(title="Test Todo 1", description="This is a test todo 1")
        todo2 = Todo(title="Test Todo 2", description="This is a test todo 2")
        db.session.add(todo1)
        db.session.add(todo2)
        db.session.commit()

        with app.test_client() as client:
            response = client.get("/todos")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(json.loads(response.data)), 2)

    def test_get_todo_by_id(self):
        todo = Todo(title="Test Todo", description="This is a test todo")
        db.session.add(todo)
        db.session.commit()

        with app.test_client() as client:
            response = client.get(f"/todos/{todo.id}")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data)["title"], "Test Todo")

    def test_create_todo(self):
        with app.test_client() as client:
            response = client.post("/todos", data=json.dumps({"title": "Test Todo", "description": "This is a test todo"}), content_type="application/json")
            self.assertEqual(response.status_code, 201)
            self.assertEqual(json.loads(response.data)["title"], "Test Todo")

    def test_update_todo(self):
        todo = Todo(title="Test Todo", description="This is a test todo")
        db.session.add(todo)
        db.session.commit()

        with app.test_client() as client:
            response = client.put(f"/todos/{todo.id}", data=json.dumps({"title": "Updated Test Todo", "description": "This is an updated test todo"}), content_type="application/json")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data)["title"], "Updated Test Todo")

    def test_delete_todo(self):
        todo = Todo(title="Test Todo", description="This is a test todo")
        db.session.add(todo)
        db.session.commit()

        with app.test_client() as client:
            response = client.delete(f"/todos/{todo.id}")
            self.assertEqual(response.status_code, 204)

if __name__ == "__main__":
    unittest.main()
```

### === test_todo_service.py ===
```python
import unittest
from todo_app.services import TodoService

class TestTodoService(unittest.TestCase):
    def test_get_all_todos(self):
        # Mock the database query
        todos = [
            {"id": 1, "title": "Test Todo 1", "description": "This is a test todo 1"},
            {"id": 2, "title": "Test Todo 2", "description": "This is a test todo 2"}
        ]

        service = TodoService()
        result = service.get_all_todos()
        self.assertEqual(result, todos)

    def test_get_todo_by_id(self):
        # Mock the database query
        todo = {"id": 1, "title": "Test Todo", "description": "This is a test todo"}

        service = TodoService()
        result = service.get_todo_by_id(1)
        self.assertEqual(result, todo)

    def test_create_todo(self):
        # Mock the database query
        todo = {"id": 1, "title": "Test Todo", "description": "This is a test todo"}

        service = TodoService()
        result = service.create_todo({"title": "Test Todo", "description": "This is a test todo"})
        self.assertEqual(result, todo)

    def test_update_todo(self):
        # Mock the database query
        todo = {"id": 1, "title": "Updated Test Todo", "description": "This is an updated test todo"}

        service = TodoService()
        result = service.update_todo(1, {"title": "Updated Test Todo", "description": "This is an updated test todo"})
        self.assertEqual(result, todo)

    def test_delete_todo(self):
        # Mock the database query
        service = TodoService()
        result = service.delete_todo(1)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
```

### === conftest.py ===
```python
import pytest
from todo_app import app, db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    db.create_all()

    with app.test_client() as client:
        yield client

    db.session.remove()
    db.drop_all()
```

### === test_todo_api_integration.py ===
```python
import pytest
from conftest import client

def test_get_all_todos(client):
    # Create some todos
    client.post("/todos", data={"title": "Test Todo 1", "description": "This is a test todo 1"})
    client.post("/todos", data={"title": "Test Todo 2", "description": "This is a test todo 2"})

    # Get all todos
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_todo_by_id(client):
    # Create a todo
    response = client.post("/todos", data={"title": "Test Todo", "description": "This is a test todo"})
    todo_id = response.json["id"]

    # Get the todo by id
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json["title"] == "Test Todo"

def test_create_todo(client):
    # Create a todo
    response = client.post("/todos", data={"title": "Test Todo", "description": "This is a test todo"})
    assert response.status_code == 201
    assert response.json["title"] == "Test Todo"

def test_update_todo(client):
    # Create a todo
    response = client.post("/todos", data={"title": "Test Todo", "description": "This is a test todo"})
    todo_id = response.json["id"]

    # Update the todo
    response = client.put(f"/todos/{todo_id}", data={"title": "Updated Test Todo", "description": "This is an updated test todo"})
    assert response.status_code == 200
    assert response.json["title"] == "Updated Test Todo"

def test_delete_todo(client):
    # Create a todo
    response = client.post("/todos", data={"title": "Test Todo", "description": "This is a test todo"})
    todo_id = response.json["id"]

    # Delete the todo
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204
```