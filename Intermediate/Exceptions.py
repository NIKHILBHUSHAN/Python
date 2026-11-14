x=-5

if x<0:
    # raise Exception("x should be positive")
    pass

assert (x>=-10),"x is less than -10"

try:
    a=5/1
    b=a+4
except ZeroDivisionError as e:
    print("Cannot divide by zero:",e)
except TypeError as e:
    print("Type mismatch:",e)
else:
    print("Runs if NO exception occurs!")
finally:
    print("Runs ALWAYS (used for resource cleanup).")

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value

def test_value(val):
    if val>100:
        raise ValueTooHighError("Value is too high!")
    if val<5:
        raise ValueTooSmallError("Value is too small!",val)

try:
    test_value(101)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(f"{e.message} Provided value: {e.value}")

def withdraw(balance,amount):
    try:
        if amount<=0:
            raise ValueError("Amount must be positive")

        if amount>balance:
            raise ValueError("Insufficient balance")

    except ValueError as e:
        print(e)

    else:
        balance-=amount
        print("Remaining balance:",balance)

    finally:
        print("Transaction completed")

withdraw(5000,2000)
withdraw(5000,0)
withdraw(5000,6000)

def dividenumbers(a,b):
    try:
        if not isinstance(a,int) or not isinstance(b,int):
            raise TypeError("Both must be integers")
        result=a/b
    except TypeError as e:
        print(e)
    except ZeroDivisionError:
        print("can not divide by zero")
    else:
        print("result:",result)
    finally:
        print("operation completed")
dividenumbers(20,5)
dividenumbers(20,0)
dividenumbers("20",5)