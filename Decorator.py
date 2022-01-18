def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        json_data = json.dumps(result)
        return json_data
        
    return wrapper
