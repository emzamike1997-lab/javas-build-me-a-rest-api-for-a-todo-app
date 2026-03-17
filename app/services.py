```python
from app.models import Todo, db

class TodoService:
    @staticmethod
    def get_all_todos():
        return Todo.query.all()

    @staticmethod
    def get_todo(todo_id):
        return Todo.query.get(todo_id)

    @staticmethod
    def create_todo(todo):
        db.session.add(todo)
        db.session.commit()
        return todo

    @staticmethod
    def update_todo(todo):
        db.session.commit()
        return todo

    @staticmethod
    def delete_todo(todo_id):
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()

todo_service = TodoService()
```

###