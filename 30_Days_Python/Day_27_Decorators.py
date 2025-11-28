# Day 27: Decorators
# ------------------

# Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class.
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

# 1. Creating a Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

print("Manual Decorator Call:")
say_whee()

# 2. Syntactic Sugar (The @ symbol)
# Python allows you to use decorators in a simpler way with the @ symbol.

@my_decorator
def say_hello():
    print("Hello!")

print("\nUsing @ Syntax:")
say_hello()

# 3. Decorating Functions with Arguments
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

print("\nDecorator with Arguments:")
greet("World")

# 4. Returning Values from Decorated Functions
def do_twice_return(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice_return
def return_greeting(name):
    print("Creating greeting...")
    return f"Hi {name}"

print("\nDecorator Returning Value:")
print(return_greeting("Adam"))
