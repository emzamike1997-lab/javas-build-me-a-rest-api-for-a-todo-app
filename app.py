```python
from flask import Flask
from config import DevelopmentConfig
from app.routes import todo_blueprint
from app.models import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)

app.register_blueprint(todo_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
```

### Running the Application
To run the application, navigate to the project directory and run the following commands:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
The application will start on `http://localhost:5000`. You can use a tool like `curl` or a REST client to test the API endpoints.

### API Endpoints
The following API endpoints are available:
- `GET /todos`: Get all todos
- `POST /todos`: Create a new todo
- `GET /todos/<int:todo_id>`: Get a todo by id
- `PUT /todos/<int:todo_id>`: Update a todo
- `DELETE /todos/<int:todo_id>`: Delete a todo

### Example Usage
To create a new todo, send a `POST` request to `http://localhost:5000/todos` with the following JSON data:
```json
{
    "title": "New Todo",
    "description": "This is a new todo"
}
```
To get all todos, send a `GET` request to `http://localhost:5000/todos`.