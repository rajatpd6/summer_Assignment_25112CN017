#include <stdio.h>

int main() {
    int original_num, num, reversed_num = 0, remainder;

    // Ask user for input
    printf("Enter an integer: ");
    scanf("%d", &num);

    // Store the original number for final comparison
    original_num = num;

    // Loop to reverse the number
    while (num != 0) {
        remainder = num % 10;                  // Extract the last digit
        reversed_num = reversed_num * 10 + remainder; // Append it to the reversed number
        num /= 10;                             // Remove the last digit from original
    }

    // Compare original number with reversed number
    if (original_num == reversed_num) {
        printf("%d is a palindrome number.\n", original_num);
    } else {
        printf("%d is not a palindrome number.\n", original_num);
    }

    return 0;
}