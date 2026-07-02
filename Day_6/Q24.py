def power_fast(x, n):
    # Handle negative exponents
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    current_product = x

    while n > 0:
        # If n is odd, multiply the current product into the result
        if n % 2 == 1:
            result *= current_product

        # Square the product and divide n by 2
        current_product *= current_product
        n //= 2

    return result


# Example usage:
base = 2
exponent = 10
print(f"{base}^{exponent} = {power_fast(base, exponent)}")
