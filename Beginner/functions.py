def hello(name="friend",age=0):
    print(f"Hello {name}, age {age}")

hello("Beau",39)
hello()

def get_user():
    return "Beau",39

name,age=get_user()

global_var="Global"

def test_scope():
    local_var="Local"
    print(global_var)

test_scope()

def outer_func():
    count=0
    def inner_func():
        nonlocal count
        count+=1
        return count
    return inner_func

counter=outer_func()
print(counter())
print(counter())
print(counter())

from functools import reduce

numbers=[1,2,3,4,5]

double=lambda a:a*2

double_numbers=list(map(lambda a:a*2,numbers))
print(double_numbers)

even_numbers=list(filter(lambda a:a%2==0,numbers))
print(even_numbers)

expenses=[("Dinner",80),("Car Repair",120)]
total=reduce(lambda a,b:a+b[1],expenses,0)
print(total)

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(3))
print(factorial(5))