# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display the number from lowest to highest. Clue: sort() function


# Create loop that keeps asking users to input number
while True:
    try:
        num = int(input("Enter a number: "))

    except ValueError:
        print("Invalid input. Stopping program.")
        break
    
# Create list to store numbers

# Stop if the input is invalid

# Display arrangement numbers from list from lowest to highest


