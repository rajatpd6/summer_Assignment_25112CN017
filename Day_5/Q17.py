def is_perfect_number(num):
    # Perfect numbers must be greater than 0
    if num <= 0:
        return False
        
    divisor_sum = 0
    
    # A proper divisor cannot be greater than num // 2
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            divisor_sum += i
            
    return divisor_sum == num

# Test the program
try:
    user_input = int(input("Enter a number to check: "))
    if is_perfect_number(user_input):
        print(f"{user_input} is a Perfect Number!")
    else:
        print(f"{user_input} is NOT a Perfect Number.")
except ValueError:
    print("Please enter a valid integer.")
