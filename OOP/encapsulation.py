class Item:
    def __init__(self,name:str,price:float):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if len(value)>10:
            raise Exception("Name cannot exceed 10 characters!")
        self.__name=value

item=Item("MyItem",750)
print(item.name)

item.name="ShortName"
print(item.name)