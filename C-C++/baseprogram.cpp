//amari grimes
//theory programming
//program that creates a list of 32 random numbers, calculates the sum, the average, the lowest and highest numbers in the list and sorted in order

#include <iostream>
#include <cstdlib>  // for rand() and srand()
#include <ctime>    // for time in order to generate new numbers everytime()
#include <algorithm> // for sorting()

using namespace std;

void create() {
    const int SIZE = 32;
    int ran[SIZE];

    // random number generator that will use different numbers everytime because of the time(0) fucntion
    srand(static_cast<unsigned int>(time(0)));

    // generating and printing the random numbers
    cout << "list of 32 random numbers:" << endl;
    for (int i = 0; i < SIZE; i++) {
        ran[i] = rand() % 101;  // random numbers between 0 and 100
        cout << ran[i] << " ";
    }
    cout << endl;

    // calculating the sum
    int sum = 0;
    for (int i = 0; i < SIZE; i++) {
        sum += ran[i];
    }
    cout << "sum of the numbers: " << sum << endl;

    // average calculation
    double average = static_cast<double>(sum) / SIZE;
    cout << "average of the numbers: " << average << endl;

    // smallest and largest number calculation
    int smallest = ran[0];
    int largest = ran[0];
    for (int i = 1; i < SIZE; i++) {
        if (ran[i] < smallest) {
            smallest = ran[i];
        }
        if (ran[i] > largest) {
            largest = ran[i];
        }
    }
    cout << "smallest number: " << smallest << endl;
    cout << "largest number: " << largest << endl;

    // sorting
    sort(ran, ran + SIZE);
    cout << "sorted list of numbers:" << endl;
    for (int i = 0; i < SIZE; i++) {
        cout << ran[i] << " ";
    }
    cout << endl;
}

int main() {
    // calling the function
    create();
    return 0;
}