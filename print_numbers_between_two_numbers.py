print("Please enter Two numbers")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

print("All the numbers between the two numbers are...")

for i in range(num1 + 1, num2):
    print(i)