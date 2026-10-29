# Default Parameter Values
def hello(name="friend",age=0):
    print(f"Hello {name}, age {age}")

hello("Beau",39)
hello()

# Returning Multiple Values
def get_user():
    return "Beau",39

name,age=get_user()

# Global vs Local Scope
global_var="Global"

def test_scope():
    local_var="Local"
    print(global_var)

test_scope()

# Nested Functions and Nonlocal
def outer_func():
    count=0
    def inner_func():
        nonlocal count
        count+=1
        return count
    return inner_func

# Closures
counter=outer_func()
print(counter())
print(counter())
print(counter())

# Lambda Functions, map(), filter(), and reduce()
from functools import reduce

numbers=[1,2,3,4,5]

# Lambda Function
double=lambda a:a*2

# map()
double_numbers=list(map(lambda a:a*2,numbers))
print(double_numbers)

# filter()
even_numbers=list(filter(lambda a:a%2==0,numbers))
print(even_numbers)

# reduce()
expenses=[("Dinner",80),("Car Repair",120)]
total=reduce(lambda a,b:a+b[1],expenses,0)
print(total)

# Recursion
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(3))
print(factorial(5))