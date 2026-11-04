import json

person={
    "name":"John",
    "age":30,
    "city":"New York",
    "hasChildren":False,
    "titles":["engineer","programmer"]
}

person_json=json.dumps(person,indent=4,sort_keys=True)
print(person_json)

with open("person.json","w") as f:
    json.dump(person,f,indent=4)

person_dict=json.loads(person_json)

with open("person.json","r") as f:
    loaded_person=json.load(f)

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user=User("Max",27)

def encode_user(obj):
    if isinstance(obj,User):
        return {"name":obj.name,"age":obj.age,obj.__class__.__name__:True}
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

user_json=json.dumps(user,default=encode_user)

class UserEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,User):
            return {"name":obj.name,"age":obj.age,obj.__class__.__name__:True}
        return super().default(obj)

user_json_b=json.dumps(user,cls=UserEncoder)

def decode_user(dct):
    if "User" in dct:
        return User(name=dct["name"],age=dct["age"])
    return dct

user_obj=json.loads(user_json,object_hook=decode_user)
print(type(user_obj),user_obj.name)