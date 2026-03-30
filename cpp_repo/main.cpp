#include <iostream>
#include "Account.h"

using namespace std;

int main(){

    Account acc1(1,1000);

    acc1.deposit(200);

    cout << "Final Balance: " << acc1.getBalance() << endl;

    return 0;
}