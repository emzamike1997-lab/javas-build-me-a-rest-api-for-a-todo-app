```python
from flask import Blueprint, request, jsonify
from app.models import Todo, TodoSchema
from app.services import todo_service

todo_blueprint = Blueprint('todo', __name__)

@todo_blueprint.route('/todos', methods=['GET'])
def get_all_todos():
    """Get all todos"""
    todos = todo_service.get_all_todos()
    schema = TodoSchema(many=True)
    return jsonify(schema.dump(todos))

@todo_blueprint.route('/todos', methods=['POST'])
def create_todo():
    """Create a new todo"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    schema = TodoSchema()
    todo = schema.load(data)
    todo_service.create_todo(todo)
    return jsonify(schema.dump(todo)), 201

@todo_blueprint.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a todo by id"""
    todo = todo_service.get_todo(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    schema = TodoSchema()
    return jsonify(schema.dump(todo))

@todo_blueprint.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a todo"""
    todo = todo_service.get_todo(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    schema = TodoSchema()
    updated_todo = schema.load(data, instance=todo)
    todo_service.update_todo(updated_todo)
    return jsonify(schema.dump(updated_todo))

@todo_blueprint.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    todo = todo_service.get_todo(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    todo_service.delete_todo(todo_id)
    return jsonify({'message': 'Todo deleted'})
```

###