# Program to print a character triangle pattern

# Take the number of rows as input from the user
rows = int(input("Enter the number of rows: "))

print("\nCharacter Triangle:")

# Outer loop handles the number of rows
for i in range(1, rows + 1):
    # Inner loop handles printing letters for each row
    for j in range(0, i):
        # 65 is the ASCII value for 'A'
        # Adding j gives us 65 ('A'), 66 ('B'), 67 ('C'), etc.
        letter = chr(65 + j)
        print(letter, end="")

    # Move to the next line after completing the current row
    print()
