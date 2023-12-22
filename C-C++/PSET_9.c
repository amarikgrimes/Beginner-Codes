
#include <stdio.h>

char getPackage();
int validPackage(char package);
int getHours();
int validHours(char package, int hours);
float calculatePkg_A(int hours);
float calculatePkg_B(int hours);
float calculatePkg_C(int hours);

int main() {
    char package;
    int hours;
    float total_cost;

    package = getPackage();

    if (!validPackage(package)) {
        printf("Invalid package selection.\n");
        return 1;
    }

    hours = getHours();

    if (!validHours(package, hours)) {
        printf("Invalid hours entered.\n");
        return 1;
    }

    if (package == 'A') {
        total_cost = calculatePkg_A(hours);
    } else if (package == 'B') {
        total_cost = calculatePkg_B(hours);
    } else if (package == 'C') {
        total_cost = calculatePkg_C(hours);
    } else {
        printf("Invalid package.\n");
        return 1;
    }

    printf("Total cost: $%.2f\n", total_cost);

    return 0;
}

char getPackage() {
    char package;
    printf("Please choose a package (A, B, or C): ");
    scanf(" %c", &package);
    return package;
}

int validPackage(char package) {
    return package == 'A' || package == 'B' || package == 'C';
}

int getHours() {
    int hours;
    printf("Please enter the total hours of internet usage: ");
    scanf("%d", &hours);
    return hours;
}

int validHours(char package, int hours) {
    return hours >= 0;
}

float calculatePkg_A(int hours) {
    float base_cost = 15;
    float total_cost;

    if (hours <= 50) {
        total_cost = base_cost;
    } else {
        int additional_hours = hours - 50;
        total_cost = base_cost + (additional_hours * 2.0);
    }

    return total_cost;
}

float calculatePkg_B(int hours) {
    float base_cost = 20;
    float total_cost;

    if (hours <= 100) {
        total_cost = base_cost;
    } else {
        int additional_hours = hours - 100;
        total_cost = base_cost + (additional_hours * 1.5);
    }

    return total_cost;
}

float calculatePkg_C(int hours) {
    float base_cost = 25;
    float total_cost;

    if (hours <= 150) {
        total_cost = base_cost;
    } else {
        int additional_hours = hours - 150;
        total_cost = base_cost + (additional_hours * 1.0);
    }

    return total_cost;
}

