#ifndef SAVINGS_ACCOUNT_H
#define SAVINGS_ACCOUNT_H

#include "Account.h"

class SavingsAccount : public Account {

private:
    double interestRate;

public:

    SavingsAccount(int id, std::string owner, double balance, double rate);

    void applyInterest();

    void print() const override;
};

#endif