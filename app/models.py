```python
# Define the Todo model

from app import db
from datetime import datetime

class Todo(db.Model):
    """Todo model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'Todo({self.title}, {self.description}, {self.completed})'

    def to_dict(self):
        """Convert the Todo object to a dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }
```

###