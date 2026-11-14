from enum import Enum

class AccountStatus(Enum):
    ACTIVE = 1
    FROZEN = 2
    CLOSED = 3

status = AccountStatus.ACTIVE

print(status)
print(status.name)
print(status.value)

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4
order=OrderStatus.SHIPPED
print(order)
print(order.name)
print(order.value)
if order==OrderStatus.SHIPPED:
    print("Your order has been shipped.")
elif order==OrderStatus.DELIVERED:
    print("Your order has been delivered.")
elif order==OrderStatus.CANCELLED:
    print("Your order has been cancelled.")
else:
    print("Your order is pending.")

