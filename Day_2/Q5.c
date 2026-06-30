#include <stdio.h>
#include <stdlib.h> // Required for abs()

int main() {
    int num, originalNum, remainder, sum = 0;

    // Accept input from the user
    printf("Enter an integer: ");
    scanf("%d", &num);

    // Store original number for final printing
    originalNum = num;

    // Handle negative numbers by converting to absolute value
    num = abs(num);

    // Loop to isolate and sum individual digits
    while (num > 0) {
        remainder = num % 10;  // Extract the last digit
        sum += remainder;      // Add the digit to sum
        num = num / 10;        // Remove the last digit
    }

    // Display the final output
    printf("The sum of the digits of %d is: %d\n", originalNum, sum);

    return 0;
}
