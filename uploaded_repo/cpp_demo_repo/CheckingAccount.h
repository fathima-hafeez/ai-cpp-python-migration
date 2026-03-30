#ifndef CHECKING_ACCOUNT_H
#define CHECKING_ACCOUNT_H

#include "Account.h"

class CheckingAccount : public Account {

private:
    double overdraftLimit;

public:

    CheckingAccount(int id, std::string owner, double balance, double limit);

    void withdraw(double amount) override;

    void print() const override;
};

#endif