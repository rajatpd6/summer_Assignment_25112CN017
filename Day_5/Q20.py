def largest_prime_factor(n):
    # Step 1: Remove all factors of 2
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    # Step 2: Check odd numbers up to the square root of n
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            max_prime = factor
            n //= factor
        factor += 2

    # Step 3: If n is still greater than 2, it is prime
    if n > 2:
        max_prime = n

    return max_prime


# Example usage:
num = 13195
result = largest_prime_factor(num)
print(f"The largest prime factor of {num} is: {result}")
