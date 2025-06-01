# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop for printing asterisks in the current row
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after printing one row
    print()
    
    # Increment the row counter
    row += 1


