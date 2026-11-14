def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("Start")
        result=func(*args,**kwargs)
        print("End")
        return result
    return wrapper

@my_decorator
def add5(x):
    return x+5

result=add5(10)

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

class CountCalls:
    def __init__(self,func):
        self.func=func
        self.num_calls=0
    def __call__(self,*args,**kwargs):
        self.num_calls+=1
        print(f"Function {self.func.__name__} executed {self.num_calls} times")
        return self.func(*args,**kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()
say_hello()