```python
# Configuration file for the todo app

class Config:
    """Base configuration class"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Configuration class for development environment"""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration class for production environment"""
    pass

class TestingConfig(Config):
    """Configuration class for testing environment"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_todo.db'
```

###