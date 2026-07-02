def print_factors(number):
    print(f"The factors of {number} are:")
    # Loop from 1 up to the number itself
    for i in range(1, number + 1):
        # Check if the number is perfectly divisible
        if number % i == 0:
            print(i)


# Example usage:
num = 24
print_factors(num)
