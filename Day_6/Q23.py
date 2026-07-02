def count_set_bits_fast(n):
    count = 0
    while n > 0:
        # This operation clears the lowest set bit
        n = n & (n - 1)
        count += 1
    return count


# Example usage:
num = 45  # Binary: 101101
print(f"Set bits in {num}: {count_set_bits_fast(num)}")
