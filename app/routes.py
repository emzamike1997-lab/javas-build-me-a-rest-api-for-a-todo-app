```python
# Define the API routes

from flask import Blueprint, request, jsonify
from app import db
from app.models import Todo
from app.utils import validate_todo

todo_blueprint = Blueprint('todo', __name__)

@todo_blueprint.route('/todos', methods=['GET'])
def get_all_todos():
    """Get all todos"""
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

@todo_blueprint.route('/todos', methods=['POST'])
def create_todo():
    """Create a new todo"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    errors = validate_todo(data)
    if errors:
        return jsonify({'error': errors}), 400
    todo = Todo(title=data['title'], description=data['description'])
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201

@todo_blueprint.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a todo by id"""
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo.to_dict())

@todo_blueprint.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a todo"""
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    errors = validate_todo(data)
    if errors:
        return jsonify({'error': errors}), 400
    todo.title = data['title']
    todo.description = data['description']
    db.session.commit()
    return jsonify(todo.to_dict())

@todo_blueprint.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted'})
```

###