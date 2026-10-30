# Exception Handling
try:
    result=2/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("No exceptions occurred.")
finally:
    print("Execution complete.")

# Custom Exceptions
class DogNotFoundException(Exception):
    pass

try:
    raise DogNotFoundException("Dog not found")
except DogNotFoundException as err:
    print(err)

# Context Managers
# File Handling with Context Manager
# with open("file.txt","r") as file:
#     content=file.read()