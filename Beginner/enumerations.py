from enum import Enum

class AccountStatus(Enum):
    ACTIVE = 1
    FROZEN = 2
    CLOSED = 3

status = AccountStatus.ACTIVE

print(status)
print(status.name)
print(status.value)