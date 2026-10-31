class Item:
    def __init__(self,name:str,price:float,quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity

    def __connect(self,smtpserver):
        print(f"Connected to {smtpserver}")

    def __prepare_body(self):
        return f"We have {self.quantity} units of {self.name}."

    def __send(self):
        print("Email sent successfully!")

    def send_email(self):
        self.__connect("[suspicious link removed]")
        self.__prepare_body()
        self.__send()

item1=Item("Laptop",1000,3)
item1.send_email()