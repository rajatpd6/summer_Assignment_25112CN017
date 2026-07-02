#include <stdio.h>
#include <math.h> // Required for the sqrt() function

int main() {
    int lower, upper, i, j, isPrime;

    // Get the range from the user
    printf("Enter lower limit: ");
    scanf("%d", &lower);
    printf("Enter upper limit: ");
    scanf("%d", &upper);

    printf("Prime numbers between %d and %d are:\n", lower, upper);

    // Loop through each number in the given range
    for (i = lower; i <= upper; i++) {
        // Numbers less than 2 are not prime
        if (i < 2) {
            continue;
        }

        // Assume the current number is prime
        isPrime = 1;

        // Check for factors up to the square root of the number
        for (j = 2; j <= sqrt(i); j++) {
            if (i % j == 0) {
                isPrime = 0; // Found a factor, so it is not prime
                break;       // Exit the inner loop early
            }
        }

        // If isPrime remains 1, the number is prime
        if (isPrime == 1) {
            printf("%d ", i);
        }
    }

    printf("\n");
    return 0;
}