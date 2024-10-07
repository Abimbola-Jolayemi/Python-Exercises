from decimal import Decimal


class Account:
    def __init__(self, name: str, pin: str, balance: Decimal=0.00):
        self.name = name.upper()
        self.pin = pin
        self.balance = balance

    def deposit (self, amount):
        if amount < Decimal(0.00):
            raise ValueError(f"It is an Invalid Amount!!!")
        self.balance += amount


account1 = Account("Abimbola", 0000)
account2 = Account("Stanley", 0000)
account1.deposit(5000)
print(account1.balance)