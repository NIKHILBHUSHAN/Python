class Item:
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

print(Item.is_integer(7))
print(Item.is_integer(7.0))
print(Item.is_integer(7.5))


class Item:
    pay_rate=0.8
    all=[]

    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0
        assert quantity>=0

        self.name=name
        self.price=price
        self.quantity=quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"


class Phone(Item):
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        super().__init__(name,price,quantity)

        assert broken_phones>=0,f"Broken Phones {broken_phones} is not >= 0!"
        self.broken_phones=broken_phones


phone1=Phone("iPhone 10",500,5,broken_phones=1)
phone2=Phone("iPhone 11",700,5,broken_phones=2)

print(Phone.all)
print(f"Phone 1 Broken Count: {phone1.broken_phones}")