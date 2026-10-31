import csv

class Item:
    pay_rate=0.8
    all=[]

    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0
        assert quantity>=0

        self.name=name
        self.price=float(price)
        self.quantity=int(quantity)

        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)

        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

Item.instantiate_from_csv()
print(Item.all)