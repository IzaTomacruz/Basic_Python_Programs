num_list = []

for i in range(10):
    num = input(f"Enter number {i + 1}: ")
    num_list.append(num)

unique_list = []
duplicate = set()

for num in num_list:
    if num not in duplicate:
        unique_list.append(num)
        duplicate.add(num)
    
print("All numbers entered:", unique_list)



