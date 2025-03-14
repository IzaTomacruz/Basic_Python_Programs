# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.
 
# Create loop that keeps asking users to input number
while True:
    try:
        num = int(input("Enter a number: "))

    except ValueError:
        print("Invalid input. Stopping program.")
        break

# Create list to store numbers

# Check if it has duplicate to display whether it is unique or duplicated

# Stop if the input is invalid


