num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

    except ValueError:
        break

if num_list:
    print("Highest number:", max(num_list))
else:
    print("No valid numbers were entered.")

