class Account {
private:
    int id;
    double balance;

public:
    Account(int i, double b){
        id = i;
        balance = b;
    }

    void deposit(double amount){
        balance += amount;
    }

    double getBalance(){
        return balance;
    }
};