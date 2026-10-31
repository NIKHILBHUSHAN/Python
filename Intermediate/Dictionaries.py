my_dict={"name":"Max","age":28,"city":"New York"}
dict_fn=dict(name="Mary",age=27,city="Boston")

print(my_dict["name"])

# print(my_dict["lastname"])
my_dict["email"]="max@xyz.com"
my_dict["email"]="coolmax@xyz.com"

del my_dict["name"]

age=my_dict.pop("age")
last_item=my_dict.popitem()

if "city" in my_dict:
    print(my_dict["city"])

try:
    print(my_dict["lastname"])
except KeyError:
    print("Key not found")

person={"name":"Alex","age":25,"role":"Developer"}

for key in person:
    print(key)

for key in person.keys():
    print(key)

for val in person.values():
    print(val)

for key,val in person.items():
    print(key,val)

dict_a={"name":"Mary","age":27,"email":"mary@xyz.com"}
dict_b={"name":"Mary","age":28,"city":"Boston"}

dict_a.update(dict_b)

valid_dict={3:9,6:36,(8,7):15}

# invalid_dict={[1,2]:"value"}