#include <iostream>
using namespace std;
int main() {
    short num1, num2;
  cout << "Enter the first number: ";
  cin >> num1;
  cout << "Enter the second number: ";
  cin >> num2;

    short sum = num1 + num2;
  
  if ((num1 > 0 && num2 > 0 && sum < 0) || (num1 < 0 && num2 < 0 &&       sum > 0)) {
  cout << "The sum is " << sum << ". An overflow has occurred." <<       endl;
    } 
  else {
       cout << "The sum is " << sum << ". No overflow has occured." << endl;
    }

    return 0;
}
