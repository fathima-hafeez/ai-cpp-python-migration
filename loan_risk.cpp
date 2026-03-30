#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;

class LoanApplicant {
private:
    string name;
    int age;
    double income;
    double loanAmount;
    int creditScore;

public:
    LoanApplicant(string n, int a, double i, double l, int c)
        : name(n), age(a), income(i), loanAmount(l), creditScore(c) {}

    double calculateRiskScore() const {
        double debtToIncome = loanAmount / income;

        double risk = 0;

        if (creditScore < 600)
            risk += 40;
        else if (creditScore < 700)
            risk += 25;
        else
            risk += 10;

        if (debtToIncome > 0.5)
            risk += 30;
        else if (debtToIncome > 0.3)
            risk += 15;

        if (age < 25)
            risk += 10;

        return risk;
    }

    string getRiskCategory() const {
        double score = calculateRiskScore();

        if (score >= 60)
            return "HIGH RISK";
        else if (score >= 35)
            return "MEDIUM RISK";
        else
            return "LOW RISK";
    }

    void printDetails() const {
        cout << "Applicant: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Income: " << income << endl;
        cout << "Loan Amount: " << loanAmount << endl;
        cout << "Credit Score: " << creditScore << endl;
        cout << "Risk Category: " << getRiskCategory() << endl;
        cout << "-----------------------------" << endl;
    }
};

vector<LoanApplicant> loadApplicants(string filename) {
    vector<LoanApplicant> applicants;
    ifstream file(filename);

    if (!file.is_open()) {
        cerr << "Error opening file." << endl;
        return applicants;
    }

    string line;

    while (getline(file, line)) {
        stringstream ss(line);
        string name;
        int age;
        double income;
        double loan;
        int credit;

        getline(ss, name, ',');
        ss >> age;
        ss.ignore();
        ss >> income;
        ss.ignore();
        ss >> loan;
        ss.ignore();
        ss >> credit;

        applicants.emplace_back(name, age, income, loan, credit);
    }

    return applicants;
}

void sortByRisk(vector<LoanApplicant>& applicants) {
    sort(applicants.begin(), applicants.end(),
         [](const LoanApplicant& a, const LoanApplicant& b) {
             return a.calculateRiskScore() > b.calculateRiskScore();
         });
}

int main() {

    vector<LoanApplicant> applicants = loadApplicants("loan_data.txt");

    if (applicants.empty()) {
        cout << "No applicants loaded." << endl;
        return 0;
    }

    sortByRisk(applicants);

    cout << "Loan Risk Assessment Report" << endl;
    cout << "============================" << endl;

    for (const auto& applicant : applicants) {
        applicant.printDetails();
    }

    return 0;
}