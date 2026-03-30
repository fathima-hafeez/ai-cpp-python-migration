class Account:
    def __init__(self, i: int, o: str, b: float):
        self._id = i
        self._owner = o
        self._balance = b

    def deposit(self, amount: float):
        if amount <= 0:
            raise RuntimeError("Invalid deposit")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise RuntimeError("Insufficient funds")
        self._balance -= amount

    def print(self):
        print(f"Account[Owner: {self._owner}, Balance: {self._balance}]")

    def getBalance(self) -> float:
        return self._balance


class CheckingAccount(Account):
    def __init__(self, id: int, owner: str, balance: float, limit: float):
        super().__init__(id, owner, balance)
        self.__overdraftLimit = limit

    def withdraw(self, amount: float):
        if amount > self._balance + self.__overdraftLimit:
            raise RuntimeError("Overdraft exceeded")
        self._balance -= amount

    def print(self):
        print(f"CheckingAccount[Owner: {self._owner}, Balance: {self._balance}, Overdraft Limit: {self.__overdraftLimit}]")


class SavingsAccount(Account):
    def __init__(self, id: int, owner: str, balance: float, rate: float):
        super().__init__(id, owner, balance)
        self.__interestRate = rate

    def applyInterest(self):
        self._balance += self._balance * self.__interestRate

    def print(self):
        print(f"SavingsAccount[Owner: {self._owner}, Balance: {self._balance}, Interest Rate: {self.__interestRate}]")


def main():
    accounts = []

    s1 = SavingsAccount(1, "Alice", 1000, 0.05)
    c1 = CheckingAccount(2, "Bob", 500, 200)

    s1.applyInterest()

    accounts.append(s1)
    accounts.append(c1)

    for a in accounts:
        a.print()


if __name__ == "__main__":
    main()