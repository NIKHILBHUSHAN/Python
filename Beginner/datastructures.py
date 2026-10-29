# List Creation and Indexing
dogs=["Roger",1,"Sid",True]
print(dogs[0])
print(dogs[-1])

# Modifying and Slicing
dogs[2]="Beau"
print(dogs[0:2])

# Common List Methods
dogs.append("Judah")
dogs.extend(["Tina",5])
dogs.insert(2,"Test")
dogs.remove("Test")
popped=dogs.pop()

# Sorting and Copying
items=["Roger","bob","Beau","Sid"]
items.sort(key=str.lower)
sorted_list=sorted(items)
items_copy=items.copy()

# Tuples
names=("Roger","Sid")

# Tuple Access and Operations
print(names[0])
print(names.index("Sid"))
print(len(names))
print("Roger" in names)

# Tuple Concatenation
new_tuple=names+("Tina","Quincy")
print(new_tuple)

# Dictionaries
dog={"name":"Roger","age":8,"color":"green"}

# Accessing Values
print(dog["name"])
print(dog.get("color","brown"))

# Updating and Adding Entries
dog["name"]="Sid"
dog["favorite_food"]="meat"

# Dictionary Methods
print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))

# Deleting Entries
popped_val=dog.pop("age")
popped_pair=dog.popitem()
del dog["color"]

# Sets
set1={"Roger","Sid"}
set2={"Roger","Luna"}

# Set Operations
intersect=set1&set2
union=set1|set2
difference=set1-set2

# Subsets and Supersets
print(set1>set2)
print(set1<union)

# Removing Duplicates from a List
numbers_list=[1,2,2,3,4,4,5]
unique_numbers=list(set(numbers_list))
print(unique_numbers)

# List Comprehensions
numbers=[1,2,3,4,5]

# List Comprehension Syntax
squares=[n**2 for n in numbers]
print(squares)

# Filtering with List Comprehension
even_squares=[n**2 for n in numbers if n%2==0]
print(even_squares)