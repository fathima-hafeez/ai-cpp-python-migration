#include <vector>
#include "Account.h"

class BankSystem {

private:
    std::vector<Account> accounts;

public:

    void addAccount(Account acc){
        accounts.push_back(acc);
    }

};