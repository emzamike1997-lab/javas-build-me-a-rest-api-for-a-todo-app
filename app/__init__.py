```python
# Initialize the Flask application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

db = SQLAlchemy()

def create_app(config_class=DevelopmentConfig):
    """Create the Flask application"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    from app import routes
    return app
```

###