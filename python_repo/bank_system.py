from account import Account

class BankSystem:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc):
        self.accounts.append(acc)