#include <iostream>
using namespace std;

int minfunc() {
    int min;
    int array[] = {10, 20, 8, 10, 5, 6};

    for (int i = 0; i<6; i++ ) {
        if (array[i] <= min)
            min = array[i];
    }

    return min;
}

int main() {
    cout << minfunc() << endl;
}
