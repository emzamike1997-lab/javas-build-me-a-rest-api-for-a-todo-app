```python
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

class TodoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        load_instance = True
```

###