class Account:
    def __init__(self, i, b):
        self.id = i
        self.balance = b

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance