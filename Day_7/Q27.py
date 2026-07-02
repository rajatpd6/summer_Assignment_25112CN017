# Program to find the sum of digits of a number using recursion
def sum_of_digits(n):
    # Base case: if the number becomes 0, return 0
    if n == 0:
        return 0
    else:
        # Extract the last digit and add it to the sum of the remaining digits
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit + sum_of_digits(remaining_digits)


# Taking input from the user
num = int(input("Enter a number: "))

# Making sure negative numbers are converted to positive for counting digits
actual_num = abs(num)

result = sum_of_digits(actual_num)
print("The sum of digits of", num, "is", result)
