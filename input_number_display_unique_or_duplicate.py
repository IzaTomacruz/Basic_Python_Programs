num_list = []

while True:
    try:
        num = int(input("Enter a number: "))

        if num in num_list:
            print("Duplicate")
        else:
            print("Unique")
            num_list.append(num)

    except ValueError:
        print("Invalid input. Stopping program.")
        break
