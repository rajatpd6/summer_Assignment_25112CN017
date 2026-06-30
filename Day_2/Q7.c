#include <stdio.h>

int main() {
    int num, rem, product = 1;

    // Prompt the user for input
    printf("Enter any number: ");
    scanf("%d", &num);

    // Handle negative numbers by converting them to positive
    if (num < 0) {
        num = -num;
    }

    // Handle the special case where the input number is 0
    if (num == 0) {
        product = 0;
    }

    // Loop to extract and multiply each digit
    while (num > 0) {
        rem = num % 10;       // Get the last digit
        product = product * rem; // Multiply the digit to the running product
        num = num / 10;       // Remove the last digit
    }

    // Display the final result
    printf("Product of digits = %d\n", product);

    return 0;
}