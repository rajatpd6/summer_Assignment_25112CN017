# Program to print a repeated-number pattern

# Take the number of rows as input from the user
rows = int(input("Enter the number of rows: "))

print("\nRepeated-Number Pattern:")

# Outer loop handles the number of rows
for i in range(1, rows + 1):
    # Inner loop runs 'i' times to print the number 'i' repeatedly
    for j in range(1, i + 1):
        print(i, end="")

    # Move to the next line after completing the current row
    print()
