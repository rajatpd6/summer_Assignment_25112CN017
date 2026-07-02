# Program to find the factorial of a number using recursion
def find_factorial(n):
    # Base case: if n is 0 or 1, factorial is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n multiplied by factorial of (n-1)
        return n * find_factorial(n - 1)


# Taking input from the user
num = int(input("Enter a number to find its factorial: "))

# Checking if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    output = find_factorial(num)
    print("The factorial of", num, "is", output)
