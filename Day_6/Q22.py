def binary_to_decimal_builtin(binary_str):
    # int(string, base) converts the string using the specified base
    return int(binary_str, 2)


# Example usage:
binary_num = "101101"
print(f"Decimal of {binary_num} is: {binary_to_decimal_builtin(binary_num)}")
