num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

    except ValueError:
        break

if num_list:
    print("Number with most duplicates:", max(set(num_list), key = num_list.count))
else:
    print("No valid numbers were entered.")

