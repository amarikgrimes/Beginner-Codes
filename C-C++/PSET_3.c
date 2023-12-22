#include <stdio.h>

int main() {
    int size, year;
    char month[size];
    double totalIncome, productSales, salesTax, countryTax, totalTax;


    printf("Enter the month:");
    scanf("%s", &month);
    
  
    printf("Enter the year: ");
    scanf("%d", &year);

    printf("Enter the total amount collected at the cash register: ");
    scanf("%lf", &totalIncome);

    // Calculate the product sales
    productSales = totalIncome / 1.06;

    // Calculate the sales tax
    salesTax = productSales * .06;

    countryTax = productSales * .025;

    totalTax = salesTax + countryTax;

    printf(" \n");
    printf("Monthly Sales Tax Report \n");
    printf("Month: %s\n", month);
    printf("Year: %d\n", year);
    printf("Total Income: $%.2lf\n", totalIncome);
    printf("Product Sales: $%.2lf\n", productSales);
    printf("Sales Tax: $%.2lf\n", salesTax);
    printf("Country Tax: $%.2lf\n", countryTax);
    printf("Total Tax: $%.2lf\n", totalTax);

    return 0;
}
