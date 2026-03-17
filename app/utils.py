```python
# Utility functions

def validate_todo(data):
    """Validate the todo data"""
    errors = []
    if not data.get('title'):
        errors.append('Title is required')
    if not data.get('description'):
        errors.append('Description is required')
    return errors
```

###