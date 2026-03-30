#include "Account.h"
#include <stdexcept>

Account::Account(int i, std::string o, double b)
    : id(i), owner(o), balance(b) {}

void Account::deposit(double amount) {

    if(amount <= 0)
        throw std::runtime_error("Invalid deposit");

    balance += amount;
}

void Account::withdraw(double amount) {

    if(amount > balance)
        throw std::runtime_error("Insufficient funds");

    balance -= amount;
}

void Account::print() const {

    std::cout << "Account[Owner: " << owner
              << ", Balance: " << balance << "]" << std::endl;
}

double Account::getBalance() const {

    return balance;
}

Account::~Account() {}