import copy 
original=[1,2,[3,4]]
shallow=copy.copy(original)
 
deep=copy.deepcopy(original)
deep[2][0]=999
print(original)
print(deep)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Company:
    def __init__(self,boss,employee):
        self.boss=boss
        self.employee=employee

p1=Person("Alex",55)
p2=Person("Joe",27)
comp=Company(p1,p2)
comp_shallow=copy.copy(comp)
comp_deep=copy.deepcopy(comp)
comp_deep.boss.age=60
print("Original boss age:",comp.boss.age)