# Inheritance
class Animal:
    def walk(self):
        print("Walking...")

# Child Class
class Dog(Animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print("Woof!")

# Instantiation and Method Access
roger=Dog("Roger",8)
print(roger.name)
roger.bark()
roger.walk()

# Polymorphism
class Cat:
    def eat(self):
        print("Eating cat food")

class Dog:
    def eat(self):
        print("Eating dog food")

animals=[Cat(),Dog()]
for animal in animals:
    animal.eat()

# Operator Overloading
class DogComparable:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __gt__(self,other):
        return self.age>other.age

roger=DogComparable("Roger",8)
sid=DogComparable("Sid",7)
print(roger>sid)