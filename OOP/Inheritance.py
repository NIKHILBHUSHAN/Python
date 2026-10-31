class Item:
    def __init__(self,name:str,price:float):
        self.name=name
        self.price=price

    def apply_discount(self):
        self.price*=0.8

class Phone(Item):
    pass

phone=Phone("Pixel",600)
phone.apply_discount()
print(f"Discounted Phone Price: ${phone.price}")