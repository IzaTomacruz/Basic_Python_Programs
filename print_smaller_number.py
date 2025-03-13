print("Please enter Two numbers") 

num1 = float(input("First number: ")) 
num2 = float(input("Second number: "))

if num1 < num2:
    print("The smaller number is", num1)
elif num1 > num2:
    print("The smaller number is", num2)
else:
    print("Both are equal")