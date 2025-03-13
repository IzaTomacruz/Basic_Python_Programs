# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Create a list where we will store our numbers
num_list = []

# Ask users to input 10 numbers
for i in range(10):
    num = input(f"Enter number {i + 1}: ")
    num_list.append(num)

# Find numbers that dont have duplicate from the list
unique_list = []

for num in num_list: 
    if num_list.count(num) == 1:
        unique_list.append(num)

# print the numbers that dont have duplicate
print(unique_list)