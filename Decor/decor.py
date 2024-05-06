def add_prefix(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Prefix: {result}"
    return wrapper

@add_prefix
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)