# Math Module
import math

print(math.sqrt(16))

# Command Line Arguments
import sys
import argparse

# sys.argv
# Usage: python script.py Beau 39
# sys.argv[1] contains "Beau"

# argparse Setup
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

    def wrapper(*args, **kwargs):
        print("Before execution")

        result = func(*args, **kwargs)

        print("After execution")

        return result

    return wrapper

def add(a, b):
    return a + b

addition=my_decorator(add)
print(addition(10,20))