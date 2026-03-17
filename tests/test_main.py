### === test_todo_model.py ===
```python
import unittest
from unittest.mock import Mock
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

### === test_todo_repository.py ===
```python
import unittest
from unittest.mock import Mock
from todo_app.repositories import TodoRepository
from todo_app.models import Todo

class TestTodoRepository(unittest.TestCase):

    def test_get_all_todos(self):
        # Arrange
        todo_repo = TodoRepository()
        todo1 = Todo(title="Test Todo 1", description="This is a test todo 1")
        todo2 = Todo(title="Test Todo 2", description="This is a test todo 2")
        todo_repo.todos = [todo1, todo2]

        # Act
        todos = todo_repo.get_all_todos()

        # Assert
        self.assertEqual(len(todos), 2)
        self.assertIn(todo1, todos)
        self.assertIn(todo2, todos)

    def test_get_todo_by_id(self):
        # Arrange
        todo_repo = TodoRepository()
        todo1 = Todo(title="Test Todo 1", description="This is a test todo 1")
        todo2 = Todo(title="Test Todo 2", description="This is a test todo 2")
        todo_repo.todos = [todo1, todo2]

        # Act
        todo = todo_repo.get_todo_by_id(1)

        # Assert
        self.assertEqual(todo, todo1)

    def test_create_todo(self):
        # Arrange
        todo_repo = TodoRepository()
        todo = Todo(title="Test Todo", description="This is a test todo")

        # Act
        todo_repo.create_todo(todo)

        # Assert
        self.assertIn(todo, todo_repo.todos)

    def test_update_todo(self):
        # Arrange
        todo_repo = TodoRepository()
        todo = Todo(title="Test Todo", description="This is a test todo")
        todo_repo.todos = [todo]

        # Act
        updated_todo = Todo(title="Updated Test Todo", description="This is an updated test todo")
        todo_repo.update_todo(updated_todo)

        # Assert
        self.assertEqual(todo_repo.todos[0].title, "Updated Test Todo")
        self.assertEqual(todo_repo.todos[0].description, "This is an updated test todo")

    def test_delete_todo(self):
        # Arrange
        todo_repo = TodoRepository()
        todo = Todo(title="Test Todo", description="This is a test todo")
        todo_repo.todos = [todo]

        # Act
        todo_repo.delete_todo(todo)

        # Assert
        self.assertEqual(len(todo_repo.todos), 0)

if __name__ == '__main__':
    unittest.main()
```

### === test_todo_service.py ===
```python
import unittest
from unittest.mock import Mock
from todo_app.services import TodoService
from todo_app.repositories import TodoRepository
from todo_app.models import Todo

class TestTodoService(unittest.TestCase):

    def test_get_all_todos(self):
        # Arrange
        todo_repo = Mock(spec=TodoRepository)
        todo_service = TodoService(todo_repo)
        todo1 = Todo(title="Test Todo 1", description="This is a test todo 1")
        todo2 = Todo(title="Test Todo 2", description="This is a test todo 2")
        todo_repo.get_all_todos.return_value = [todo1, todo2]

        # Act
        todos = todo_service.get_all_todos()

        # Assert
        self.assertEqual(len(todos), 2)
        self.assertIn(todo1, todos)
        self.assertIn(todo2, todos)

    def test_get_todo_by_id(self):
        # Arrange
        todo_repo = Mock(spec=TodoRepository)
        todo_service = TodoService(todo_repo)
        todo = Todo(title="Test Todo", description="This is a test todo")
        todo_repo.get_todo_by_id.return_value = todo

        # Act
        result = todo_service.get_todo_by_id(1)

        # Assert
        self.assertEqual(result, todo)

    def test_create_todo(self):
        # Arrange
        todo_repo = Mock(spec=TodoRepository)
        todo_service = TodoService(todo_repo)
        todo = Todo(title="Test Todo", description="This is a test todo")

        # Act
        todo_service.create_todo(todo)

        # Assert
        todo_repo.create_todo.assert_called_once_with(todo)

    def test_update_todo(self):
        # Arrange
        todo_repo = Mock(spec=TodoRepository)
        todo_service = TodoService(todo_repo)
        todo = Todo(title="Test Todo", description="This is a test todo")

        # Act
        todo_service.update_todo(todo)

        # Assert
        todo_repo.update_todo.assert_called_once_with(todo)

    def test_delete_todo(self):
        # Arrange
        todo_repo = Mock(spec=TodoRepository)
        todo_service = TodoService(todo_repo)
        todo = Todo(title="Test Todo", description="This is a test todo")

        # Act
        todo_service.delete_todo(todo)

        # Assert
        todo_repo.delete_todo.assert_called_once_with(todo)

if __name__ == '__main__':
    unittest.main()
```

### === test_todo_controller.py ===
```python
import unittest
from unittest.mock import Mock
from todo_app.controllers import TodoController
from todo_app.services import TodoService
from todo_app.models import Todo

class TestTodoController(unittest.TestCase):

    def test_get_all_todos(self):
        # Arrange
        todo_service = Mock(spec=TodoService)
        todo_controller = TodoController(todo_service)
        todo1 = Todo(title="Test Todo 1", description="This is a test todo 1")
        todo2 = Todo(title="Test Todo 2", description="This is a test todo 2")
        todo_service.get_all_todos.return_value = [todo1, todo2]

        # Act
        response = todo_controller.get_all_todos()

        # Assert
        self.assertEqual(len(response), 2)
        self.assertIn(todo1, response)
        self.assertIn(todo2, response)

    def test_get_todo_by_id(self):
        # Arrange
        todo_service = Mock(spec=TodoService)
        todo_controller = TodoController(todo_service)
        todo = Todo(title="Test Todo", description="This is a test todo")
        todo_service.get_todo_by_id.return_value = todo

        # Act
        response = todo_controller.get_todo_by_id(1)

        # Assert
        self.assertEqual(response, todo)

    def test_create_todo(self):
        # Arrange
        todo_service = Mock(spec=TodoService)
        todo_controller = TodoController(todo_service)
        todo = Todo(title="Test Todo", description="This is a test todo")

        # Act
        todo_controller.create_todo(todo)

        # Assert
        todo_service.create_todo.assert_called_once_with(todo)

    def test_update_todo(self):
        # Arrange
        todo_service = Mock(spec=TodoService)
        todo_controller = TodoController(todo_service)
        todo = Todo(title="Test Todo", description="This is a test todo")

        # Act
        todo_controller.update_todo(todo)

        # Assert
        todo_service.update_todo.assert_called_once_with(todo)

    def test_delete_todo(self):
        # Arrange
        todo_service = Mock(spec=TodoService)
        todo_controller = TodoController(todo_service)
        todo = Todo(title="Test Todo", description="This is a test todo")

        # Act
        todo_controller.delete_todo(todo)

        # Assert
        todo_service.delete_todo.assert_called_once_with(todo)

if __name__ == '__main__':
    unittest.main()
```

### === test_api.py ===
```python
import unittest
from unittest.mock import Mock
from todo_app.api import app
import json

class TestAPI(unittest.TestCase):

    def test_get_all_todos(self):
        # Arrange
        client = app.test_client()

        # Act
        response = client.get('/todos')

        # Assert
        self.assertEqual(response.status_code, 200)

    def test_get_todo_by_id(self):
        # Arrange
        client = app.test_client()

        # Act
        response = client.get('/todos/1')

        # Assert
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        # Arrange
        client = app.test_client()
        todo = {'title': 'Test Todo', 'description': 'This is a test todo'}

        # Act
        response = client.post('/todos', data=json.dumps(todo), content_type='application/json')

        # Assert
        self.assertEqual(response.status_code, 201)

    def test_update_todo(self):
        # Arrange
        client = app.test_client()
        todo = {'title': 'Updated Test Todo', 'description': 'This is an updated test todo'}

        # Act
        response = client.put('/todos/1', data=json.dumps(todo), content_type='application/json')

        # Assert
        self.assertEqual(response.status_code, 200)

    def test_delete_todo(self):
        # Arrange
        client = app.test_client()

        # Act
        response = client.delete('/todos/1')

        # Assert
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
```

These tests cover the following scenarios:

- Unit tests for the Todo model
- Unit tests for the Todo repository
- Unit tests for the Todo service
- Unit tests for the Todo controller
- Integration tests for the API endpoints

Note: These tests are just examples and may need to be modified to fit the specific requirements of your application. Additionally, you may need to add more tests to cover all the scenarios.