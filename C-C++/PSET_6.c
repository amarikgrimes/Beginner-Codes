#include <stdio.h>

float calculateDistance(float speed, int time) {
    return speed * time;
}

void displayMenu() {
    printf("Select a Medium:\n");
    printf("1. Carbon Dioxide\n");
    printf("2. Air\n");
    printf("3. Helium\n");
    printf("4. Hydrogen\n");
}

int getGasChoice() {
    int choice;
    while (1) {
        printf("Enter your choice (1-4): ");
        if (scanf("%d", &choice) == 1 && choice >= 1 && choice <= 4) {
            return choice;
        }
        printf("Invalid choice. Please enter a number between 1 and 4.\n");
        // Clear input buffer
        while (getchar() != '\n');
    }
}

int getTime() {
    int time;
    while (1) {
        printf("Enter the time in seconds (0-30): ");
        if (scanf("%d", &time) == 1 && time >= 0 && time <= 30) {
            return time;
        }
        printf("Invalid time. Please enter a number between 0 and 30.\n");
        // Clear input buffer
        while (getchar() != '\n');
    }
}

int main() {
    float gasSpeeds[] = {258.0, 331.5, 972.0, 1270.0};

    displayMenu();
    int choice = getGasChoice();
    float speed = gasSpeeds[choice - 1];
    int time = getTime();
    float distance = calculateDistance(speed, time);

    printf("The sound source was approximately %.2f meters away.\n", distance);

    return 0;
}
