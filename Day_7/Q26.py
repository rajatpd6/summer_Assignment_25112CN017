## Q 26)Write a program to Recursive Fibonacci. 
# Program to find the Nth Fibonacci number using recursion
def fibonacci(n):
    # Base case 1: The 0th Fibonacci number is 0
    if n == 0:
        return 0
    # Base case 2: The 1st Fibonacci number is 1
    elif n == 1:
        return 1
    # Recursive case: Sum of the two previous numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Taking input from the user
terms = int(input("Enter how many terms of Fibonacci series you want: "))

if terms <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    print("Fibonacci series:")
    # Loop to print the series from index 0 up to terms-1
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()  # For a new line at the end
