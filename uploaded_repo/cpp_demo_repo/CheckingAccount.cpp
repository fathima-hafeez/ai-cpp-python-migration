#include "CheckingAccount.h"
#include <stdexcept>

CheckingAccount::CheckingAccount(int id, std::string owner, double balance, double limit)
    : Account(id, owner, balance), overdraftLimit(limit) {}

void CheckingAccount::withdraw(double amount) {

    if(amount > balance + overdraftLimit)
        throw std::runtime_error("Overdraft exceeded");

    balance -= amount;
}

void CheckingAccount::print() const {

    std::cout << "CheckingAccount[Owner: " << owner
              << ", Balance: " << balance
              << ", Overdraft Limit: " << overdraftLimit << "]"
              << std::endl;
}