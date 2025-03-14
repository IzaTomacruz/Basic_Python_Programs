num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

    except ValueError:
        break

if num_list:
    average = sum(num_list) / len(num_list)
    print("Average:", average)
else:
    print("No valid numbers were entered.")


