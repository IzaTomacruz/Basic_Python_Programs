num_list = []

for i in range(10):
    num = input(f"Enter number {i + 1}: ")
    num_list.append(num)

unique_list = []

for num in num_list: 
    if num_list.count(num) == 1:
        unique_list.append(num)

if unique_list:
    print("All unique numbers: ",unique_list)
else:
    print("No unique numbers are inputed")