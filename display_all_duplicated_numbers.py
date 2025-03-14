num_list = []

for i in range(10):
    num = input(f"Enter number {i + 1}: ")
    num_list.append(num)

duplicate_list = set()

for num in num_list:
    if num_list.count(num) > 1:
        duplicate_list.add(num)

print("Numbers with duplicates:", duplicate_list)
