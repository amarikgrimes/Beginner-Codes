#include <stdio.h>

float calculate_bmi(float weight, float height) {
    float bmi = (weight * 703) / (height * height);
    return bmi;
}

const char* determine_weight_category(float bmi) {
    if (bmi < 18.5) {
        return "underweight";
    } else if (bmi >= 18.5 && bmi <= 25) {
        return "optimal weight";
    } else {
        return "overweight";
    }
}

int main() {
    float weight, height;
    
    // Get user input
    printf("Enter weight in lbs: ");
    scanf("%f", &weight);
    printf("Enter height in inches: ");
    scanf("%f", &height);

    // Calculate BMI
    float bmi = calculate_bmi(weight, height);

    // Determine weight category
    const char* weight_category = determine_weight_category(bmi);

    // Display results
    printf("Weight: %.2f lbs\n", weight);
    printf("Height: %.2f inches\n", height);
    printf("BMI: %.2f\n", bmi);
    printf("Weight category: %s\n", weight_category);

    return 0;
}
