# Program to print a number triangle pattern

# Take the number of rows as input from the user
rows = int(input("Enter the number of rows: "))

print("\nNumber Triangle:")

# Outer loop handles the number of rows
for i in range(1, rows + 1):
    # Inner loop handles printing numbers from 1 up to the current row number
    for j in range(1, i + 1):
        print(j, end="")

    # Move to the next line after completing the current row
    print()
