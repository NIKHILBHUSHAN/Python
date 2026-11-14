dogs=["Roger",1,"Sid",True]
print(dogs[0])
print(dogs[-1])

dogs[2]="Beau"
print(dogs[0:2])

dogs.append("Judah")
dogs.extend(["Tina",5])
dogs.insert(2,"Test")
dogs.remove("Test")
popped=dogs.pop()

items=["Roger","bob","Beau","Sid"]
items.sort(key=str.lower)
sorted_list=sorted(items)
items_copy=items.copy()

names=("Roger","Sid")

print(names[0])
print(names.index("Sid"))
print(len(names))
print("Roger" in names)

new_tuple=names+("Tina","Quincy")
print(new_tuple)

dog={"name":"Roger","age":8,"color":"green"}

print(dog["name"])
print(dog.get("color","brown"))

dog["name"]="Sid"
dog["favorite_food"]="meat"

print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))

popped_val=dog.pop("age")
popped_pair=dog.popitem()
del dog["color"]

set1={"Roger","Sid"}
set2={"Roger","Luna"}

intersect=set1&set2
union=set1|set2
difference=set1-set2

print(set1>set2)
print(set1<union)

numbers_list=[1,2,2,3,4,4,5]
unique_numbers=list(set(numbers_list))
print(unique_numbers)

numbers=[1,2,3,4,5]

squares=[n**2 for n in numbers]
print(squares)

even_squares=[n**2 for n in numbers if n%2==0]
print(even_squares)