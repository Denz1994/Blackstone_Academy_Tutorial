#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    double mealPrice;
    int tip;
    int tax;

    cin>>mealPrice>>tip>>tax;
    //cin>> tip;
    //cin>> tax;
    //cout<<tip<<endl<<tax<<endl<<endl<<endl;

    double tipAmount=(tip*.01)*mealPrice;
    double taxAmount=(tax*.01)*mealPrice;
    double finalAmount=tipAmount+taxAmount+mealPrice;
    //cout<<"tip amount "<<tipAmount<<endl;
    //cout<<"taxAmount "<<taxAmount<<endl;
    //cout<<"finalAmount"<<finalAmount<<endl;

    cout<<"The final price of the meal is $"<< roundf(finalAmount)<<".";

    return 0;
}
