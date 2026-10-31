print(len("Python"))
print(len(["a","b","c"]))

class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def apply_discount(self):
        self.price*=0.8

class Keyboard(Item):
    def apply_discount(self):
        self.price*=0.7

items=[
    Item("Generic Item",100),
    Keyboard("Gaming Keyboard",100)
]

for item in items:
    item.apply_discount()
    print(f"{item.name} final price: ${item.price}")