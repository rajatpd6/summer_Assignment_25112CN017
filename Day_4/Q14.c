#include <stdio.h>

// Function to find the nth Fibonacci number
unsigned long long get_nth_fibonacci(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;

    unsigned long long prev2 = 0; // Represents F(n-2)
    unsigned long long prev1 = 1; // Represents F(n-1)
    unsigned long long current = 0;

    for (int i = 2; i <= n; i++) {
        current = prev1 + prev2;   // F(n) = F(n-1) + F(n-2)
        prev2 = prev1;            // Update F(n-2) for next iteration
        prev1 = current;          // Update F(n-1) for next iteration
    }

    return current;
}

int main() {
    int n;

    printf("Enter the value of n: ");
    if (scanf("%d", &n) != 1 || n < 0) {
        printf("Please enter a valid non-negative integer.\n");
        return 1;
    }

    unsigned long long result = get_nth_fibonacci(n);
    printf("The %dth Fibonacci term is: %llu\n", n, result);

    return 0;
}
