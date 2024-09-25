//amari grimes
//theory programming
//this program solves a quadratic equation using the a,b, and c inputed by the user, it will find the real roots, complex roots and double root. this program will loop 5 times. 

#include <iostream>
#include <cmath>  // for sqrt()
using namespace std;

void solvequad() {
    double a, b, c;

    // asking the user for a, b, c
    cout << "enter 'a' (cannot be zero): ";
    cin >> a;
    while (a == 0) {
        cout << "'a' cannot be zero. please enter a non-zero value for 'a': ";
        cin >> a;
    }

    cout << "please enter b: ";
    cin >> b;
    cout << "please enter c: ";
    cin >> c;

    // discriminant calculation
    double disc = b * b - 4 * a * c;
    double root1, root2;

    if (disc > 0) {
        // two distinct real root calculations
        root1 = (-b + sqrt(disc)) / (2 * a);
        root2 = (-b - sqrt(disc)) / (2 * a);
        cout << "the roots are real and different! root 1 & 2 are: " << root1 << " & " << root2 << endl;
    } 
    else if (disc == 0) {
        // one real root calculations
        root1 = -b / (2 * a);
        cout << "the roots are real and the same (it's double root!). root 1 & 2 are: " << root1 << endl;
    } 
    else {
        // complex root calculations
        double real = -b / (2 * a);
        double imaginary = sqrt(-disc) / (2 * a);
        cout << "the roots are complex and different." << endl;
        cout << "root 1 = " << real << " + " << imaginary << "i" << endl;
        cout << "root 2 = " << real << " - " << imaginary << "i" << endl;
    }

    cout << "----------------------------------" << endl;
}

int main() {
    // loop 5 times
    for (int i = 0; i < 5; i++) {
        cout << "solving quadratic equation #" << i + 1 << endl;
        solvequad();
    }

    return 0;
}
