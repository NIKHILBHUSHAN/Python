item1_name="Phone"
item1_price=100
item1_quantity=5
item1_price_total=item1_price*item1_quantity

class Item:
    def calculate_total_price(self,x,y):
        return x*y

item1=Item()
item1.name="Phone"
item1.price=100
item1.quantity=5

item2=Item()
item2.name="Laptop"
item2.price=1000
item2.quantity=3

print(f"Item 1 Total: ${item1.calculate_total_price(item1.price,item1.quantity)}")
print(f"Item 2 Total: ${item2.calculate_total_price(item2.price,item2.quantity)}")