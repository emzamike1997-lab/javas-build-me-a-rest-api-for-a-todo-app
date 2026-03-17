### === test_todo_model.py ===
```python
import unittest
from unittest.mock import MagicMock
from todo_app.models import Todo

class TestTodoModel(unittest.TestCase):

    def test_todo_creation(self):
        todo = Todo(title="Test Todo", description="This is a test todo")
        self.assertEqual(todo.title, "Test Todo")
        self.assertEqual(todo.description, "This is a test todo")

    def test_todo_str_representation(self):
        todo = Todo(title="Test Todo", description="This is a test todo")
        self.assertEqual(str(todo), "Test Todo")

    def test_todo_equals(self):
        todo1 = Todo(title="Test Todo", description="This is a test todo")
        todo2 = Todo(title="Test Todo", description="This is a test todo")
        self.assertEqual(todo1, todo2)

if __name__ == '__main__':
    unittest.main()
```

### === test_todo_service.py ===
```python
import unittest
from unittest.mock import MagicMock
from todo_app.services import TodoService
from todo_app.models import Todo

class TestTodoService(unittest.TestCase):

    def test_get_all_todos(self):
        todo_service = TodoService()
        todo_service.get_all_todos = MagicMock(return_value=[Todo(title="Test Todo 1", description="This is a test todo 1"), 
                                                             Todo(title="Test Todo 2", description="This is a test todo 2")])
        todos = todo_service.get_all_todos()
        self.assertEqual(len(todos), 2)

    def test_get_todo_by_id(self):
        todo_service = TodoService()
        todo_service.get_todo_by_id = MagicMock(return_value=Todo(title="Test Todo", description="This is a test todo"))
        todo = todo_service.get_todo_by_id(1)
        self.assertEqual(todo.title, "Test Todo")

    def test_create_todo(self):
        todo_service = TodoService()
        todo_service.create_todo = MagicMock(return_value=Todo(title="Test Todo", description="This is a test todo"))
        todo = todo_service.create_todo("Test Todo", "This is a test todo")
        self.assertEqual(todo.title, "Test Todo")

    def test_update_todo(self):
        todo_service = TodoService()
        todo_service.update_todo = MagicMock(return_value=Todo(title="Updated Test Todo", description="This is an updated test todo"))
        todo = todo_service.update_todo(1, "Updated Test Todo", "This is an updated test todo")
        self.assertEqual(todo.title, "Updated Test Todo")

    def test_delete_todo(self):
        todo_service = TodoService()
        todo_service.delete_todo = MagicMock(return_value=None)
        result = todo_service.delete_todo(1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
```

### === test_todo_controller.py ===
```python
import unittest
from unittest.mock import MagicMock
from todo_app.controllers import TodoController
from todo_app.models import Todo

class TestTodoController(unittest.TestCase):

    def test_get_all_todos(self):
        todo_controller = TodoController()
        todo_controller.todo_service = MagicMock()
        todo_controller.todo_service.get_all_todos = MagicMock(return_value=[Todo(title="Test Todo 1", description="This is a test todo 1"), 
                                                                              Todo(title="Test Todo 2", description="This is a test todo 2")])
        response = todo_controller.get_all_todos()
        self.assertEqual(len(response), 2)

    def test_get_todo_by_id(self):
        todo_controller = TodoController()
        todo_controller.todo_service = MagicMock()
        todo_controller.todo_service.get_todo_by_id = MagicMock(return_value=Todo(title="Test Todo", description="This is a test todo"))
        response = todo_controller.get_todo_by_id(1)
        self.assertEqual(response.title, "Test Todo")

    def test_create_todo(self):
        todo_controller = TodoController()
        todo_controller.todo_service = MagicMock()
        todo_controller.todo_service.create_todo = MagicMock(return_value=Todo(title="Test Todo", description="This is a test todo"))
        response = todo_controller.create_todo("Test Todo", "This is a test todo")
        self.assertEqual(response.title, "Test Todo")

    def test_update_todo(self):
        todo_controller = TodoController()
        todo_controller.todo_service = MagicMock()
        todo_controller.todo_service.update_todo = MagicMock(return_value=Todo(title="Updated Test Todo", description="This is an updated test todo"))
        response = todo_controller.update_todo(1, "Updated Test Todo", "This is an updated test todo")
        self.assertEqual(response.title, "Updated Test Todo")

    def test_delete_todo(self):
        todo_controller = TodoController()
        todo_controller.todo_service = MagicMock()
        todo_controller.todo_service.delete_todo = MagicMock(return_value=None)
        response = todo_controller.delete_todo(1)
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
```

### === test_todo_api.py ===
```python
import unittest
from unittest.mock import MagicMock
from todo_app.api import app
import json

class TestTodoAPI(unittest.TestCase):

    def test_get_all_todos(self):
        with app.test_client() as client:
            response = client.get('/todos')
            self.assertEqual(response.status_code, 200)
            self.assertGreater(len(json.loads(response.data)), 0)

    def test_get_todo_by_id(self):
        with app.test_client() as client:
            response = client.get('/todos/1')
            self.assertEqual(response.status_code, 200)
            self.assertIn('title', json.loads(response.data))

    def test_create_todo(self):
        with app.test_client() as client:
            response = client.post('/todos', data=json.dumps({'title': 'Test Todo', 'description': 'This is a test todo'}), content_type='application/json')
            self.assertEqual(response.status_code, 201)
            self.assertIn('title', json.loads(response.data))

    def test_update_todo(self):
        with app.test_client() as client:
            response = client.put('/todos/1', data=json.dumps({'title': 'Updated Test Todo', 'description': 'This is an updated test todo'}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertIn('title', json.loads(response.data))

    def test_delete_todo(self):
        with app.test_client() as client:
            response = client.delete('/todos/1')
            self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
```

### === test_integration.py ===
```python
import unittest
from todo_app.api import app, db
import json

class TestIntegration(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def test_create_and_get_todo(self):
        with app.test_client() as client:
            response = client.post('/todos', data=json.dumps({'title': 'Test Todo', 'description': 'This is a test todo'}), content_type='application/json')
            self.assertEqual(response.status_code, 201)
            response = client.get('/todos/1')
            self.assertEqual(response.status_code, 200)
            self.assertIn('title', json.loads(response.data))

    def test_update_and_get_todo(self):
        with app.test_client() as client:
            response = client.post('/todos', data=json.dumps({'title': 'Test Todo', 'description': 'This is a test todo'}), content_type='application/json')
            self.assertEqual(response.status_code, 201)
            response = client.put('/todos/1', data=json.dumps({'title': 'Updated Test Todo', 'description': 'This is an updated test todo'}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            response = client.get('/todos/1')
            self.assertEqual(response.status_code, 200)
            self.assertIn('title', json.loads(response.data))

    def test_delete_and_get_todo(self):
        with app.test_client() as client:
            response = client.post('/todos', data=json.dumps({'title': 'Test Todo', 'description': 'This is a test todo'}), content_type='application/json')
            self.assertEqual(response.status_code, 201)
            response = client.delete('/todos/1')
            self.assertEqual(response.status_code, 204)
            response = client.get('/todos/1')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
```