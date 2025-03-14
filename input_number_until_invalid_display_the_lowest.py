num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break  # Stop asking when input is invalid

if num_list:
    print("Lowest number:", min(num_list))
else:
    print("No valid numbers were entered.")

