class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print("Woof!")

roger=Dog("Roger",8)
print(roger.name)
roger.bark()
roger.walk()

class Cat:
    def eat(self):
        print("Eating cat food")

class Dog:
    def eat(self):
        print("Eating dog food")

animals=[Cat(),Dog()]
for animal in animals:
    animal.eat()

class DogComparable:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __gt__(self,other):
        return self.age>other.age

roger=DogComparable("Roger",8)
sid=DogComparable("Sid",7)
print(roger>sid)

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        return self.age>other.age
    
    def __repr__(self):
        return f'Student({self.name},{self.age})'
    def __str__(self):
            return f'{self.name} is {self.age} years old'
student1=student("Beau",39)
student2=student("Quincy",20)
print(student1>student2)
print(student1)

