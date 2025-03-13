total = float(input("Number 1: "))

for i in range(1,10):
    number = float(input(f"Number {i + 1}: "))
    total -= number

print("The total is", total)