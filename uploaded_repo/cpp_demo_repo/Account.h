#ifndef ACCOUNT_H
#define ACCOUNT_H

#include <string>
#include <iostream>

class Account {

protected:
    int id;
    std::string owner;
    double balance;

public:

    Account(int i, std::string o, double b);

    virtual void deposit(double amount);

    virtual void withdraw(double amount);

    virtual void print() const;

    double getBalance() const;

    virtual ~Account();
};

#endif