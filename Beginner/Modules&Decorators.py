# Math Module
import math

print(math.sqrt(16))

 
import sys
import argparse

# sys.argv
# Usage: python script.py Beau 39
# sys.argv[1] contains "Beau"


parser=argparse.ArgumentParser(description="Prints dog colors")
parser.add_argument("-c","--color",required=True,choices=["red","yellow"],help="color choice")

# args=parser.parse_args()
# print(args.color)

# Decorators
def log_time(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@log_time
def hello():
    print("Hello World!")

hello()




def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("function Started")
        result=func(*args,**kwargs)
        print("function ended")
        return result
    return wrapper
"""def calculate(a,b):
    return a+b
result=my_decorator(calculate)
result(30,50)"""
@my_decorator
def calculate(a,b):
    return a+b
print(calculate(30,50))