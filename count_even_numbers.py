print('Please enter Ten numbers')

even_count = 0

for i in range(10):
    number = int(input(f"Number {i + 1}: "))

    if number % 2 == 0:
        even_count += 1

print("Total even numbers:", even_count)
