# Helper function that carries the reversed number in 'rev'
def reverse_helper(n, rev):
    # Base case: when n becomes 0, return the accumulated reversed number
    if n == 0:
        return rev
    else:
        # Extract the last digit
        last_digit = n % 10
        # Build the reversed number: shift previous digits left and add the new digit
        rev = (rev * 10) + last_digit
        # Recursive call with the remaining digits
        return reverse_helper(n // 10, rev)


def reverse_number(n):
    # If the number is 0, the reverse is just 0
    if n == 0:
        return 0

    # Handle negative numbers by working with positive values first
    is_negative = n < 0
    abs_num = abs(n)

    # Call the helper starting with an initial reversed value of 0
    reversed_abs = reverse_helper(abs_num, 0)

    # Put the negative sign back if the original number was negative
    if is_negative:
        return -reversed_abs
    else:
        return reversed_abs


# Taking input from the user
num = int(input("Enter a number to reverse: "))

result = reverse_number(num)
print("The reversed number is:", result)
