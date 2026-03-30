#include <vector>
#include "SavingsAccount.h"
#include "CheckingAccount.h"

int main(){

    std::vector<Account*> accounts;

    SavingsAccount s1(1,"Alice",1000,0.05);
    CheckingAccount c1(2,"Bob",500,200);

    s1.applyInterest();

    accounts.push_back(&s1);
    accounts.push_back(&c1);

    for(auto a : accounts){
        a->print();
    }

    return 0;
}