#include <stdio.h>
#include <math.h>

int main() {
    int start, end, i, temp, remainder, digits, sum;

    // Ask user for the range limits
    printf("Enter lower limit of the range: ");
    scanf("%d", &start);
    printf("Enter upper limit of the range: ");
    scanf("%d", &end);

    printf("Armstrong numbers between %d and %d are:\n", start, end);

    // Loop through each number in the given range
    for (i = start; i <= end; i++) {
        // Step 1: Count the number of digits
        digits = 0;
        temp = i;
        while (temp != 0) {
            digits++;
            temp /= 10;
        }

        // Step 2: Calculate the sum of the digits raised to the power of 'digits'
        sum = 0;
        temp = i;
        while (temp != 0) {
            remainder = temp % 10;
            
            // round or lround prevents precision loss from the pow() function
            sum += lround(pow(remainder, digits)); 
            
            temp /= 10;
        }

        // Step 3: Check if the sum matches the original number
        if (sum == i) {
            printf("%d ", i);
        }
    }

    printf("\n");
    return 0;
}
