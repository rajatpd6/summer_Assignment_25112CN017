def decimal_to_binary_builtin(n):
    # bin() returns a string starting with '0b'
    # [2:] removes the '0b' prefix
    return bin(n)[2:]


# Example usage:
num = 45
print(f"Binary of {num} is: {decimal_to_binary_builtin(num)}")
