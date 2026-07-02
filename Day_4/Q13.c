#include <stdio.h>

int main() {
    int n;
    unsigned long long first = 0, second = 1, next;

    // Prompt user for the number of terms
    printf("Enter the number of terms: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Please enter a valid positive integer.\n");
        return 1;
    }

    printf("Fibonacci Series: ");

    for (int i = 1; i <= n; i++) {
        // Print the current term
        printf("%llu", first);
        
        // Add a comma after all elements except the last one
        if (i < n) {
            printf(", ");
        }

        // Calculate the next term and shift variables
        next = first + second;
        first = second;
        second = next;
    }

    printf("\n");
    return 0;
}
