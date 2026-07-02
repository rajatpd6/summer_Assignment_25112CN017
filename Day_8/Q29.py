# Program to print a half pyramid pattern using stars

# Take the number of rows as input from the user
rows = int(input("Enter the number of rows: "))

print("\nHalf Pyramid Pattern:")

# Outer loop handles the number of rows
for i in range(1, rows + 1):
    # Inner loop handles printing stars in each row
    for j in range(1, i + 1):
        print("*", end=" ")

    # Move to the next line after finishing the current row.
    print()
