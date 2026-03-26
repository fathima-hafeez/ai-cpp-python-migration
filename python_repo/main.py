from account import Account

def main():
    acc1 = Account(1, 1000)
    acc1.deposit(200)
    print("Final Balance:", acc1.get_balance())

if __name__ == "__main__":
    main()