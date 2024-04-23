def add_prefix(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@add_prefix
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)