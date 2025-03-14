num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)
        
    except ValueError:
        break 

if num_list:
    num_list.sort() 
    print("Numbers from lowest to highest:", num_list)
else:
    print("No valid numbers were entered.")



