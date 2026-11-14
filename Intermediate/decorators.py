import functools
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("start")
        result=func(*args,**kwargs)
        print("end")
        return result
    return wrapper

def add5(a):
    return a+5

print(add5(5))

def repeat(num_times=3):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                res=func(*args,**kwargs)
            return res
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alex")