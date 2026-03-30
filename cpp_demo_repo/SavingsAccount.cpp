#include "SavingsAccount.h"

SavingsAccount::SavingsAccount(int id, std::string owner, double balance, double rate)
    : Account(id, owner, balance), interestRate(rate) {}

void SavingsAccount::applyInterest() {

    balance += balance * interestRate;
}

void SavingsAccount::print() const {

    std::cout << "SavingsAccount[Owner: " << owner
              << ", Balance: " << balance
              << ", Interest Rate: " << interestRate << "]"
              << std::endl;
}