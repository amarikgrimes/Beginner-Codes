#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to compute the monthly payment
void compute_monthly_payment(double loan_amount, double annual_interest_rate, int num_payments, double* monthly_payment, double* amount_paid_back, double* interest_paid) {
    double monthly_interest_rate = annual_interest_rate / 100 / 12;
    *monthly_payment = (loan_amount * monthly_interest_rate) / (1 - pow(1 + monthly_interest_rate, -num_payments));
    *amount_paid_back = *monthly_payment * num_payments;
    *interest_paid = *amount_paid_back - loan_amount;
}

int main() {
    double loan_amount, annual_interest_rate, monthly_payment, amount_paid_back, interest_paid;
    int num_payments;

    // Get input from the user and validate it
    while (1) {
        printf("Enter the loan amount: $");
        if (scanf("%lf", &loan_amount) != 1) {
            printf("Invalid input. Please enter a valid number.\n");
            fflush(stdin);
            continue;
        }
        printf("Enter the annual interest rate: ");
        if (scanf("%lf", &annual_interest_rate) != 1) {
            printf("Invalid input. Please enter a valid number.\n");
            fflush(stdin);
            continue;
        }
        printf("Enter the number of payments: ");
        if (scanf("%d", &num_payments) != 1) {
            printf("Invalid input. Please enter a valid number.\n");
            fflush(stdin);
            continue;
        }
        break;
    }

    // Compute the monthly payment, amount paid back, and interest paid
    compute_monthly_payment(loan_amount, annual_interest_rate, num_payments, &monthly_payment, &amount_paid_back, &interest_paid);

    // Display the results
    printf("\nLoan Amount: $ %.2f\n", loan_amount);
    printf("Annual Interest Rate: %.2f%%\n", annual_interest_rate);
    printf("Number of Payments: %d\n", num_payments);
    printf("Monthly Payment: $ %.2f\n", monthly_payment);
    printf("Amount Paid Back: $ %.2f\n", amount_paid_back);
    printf("Interest Paid: $ %.2f\n", interest_paid);

    return 0;
}
