# Find the second largest number in a list.

my_list=[1,1,2]

largest = my_list[0]
second_largest = None

for num in my_list:
    if num > largest:
        largest = num

for num in my_list:
    if num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num

if second_largest is None:
    print("There is no second largest number.")
else:
    print("Largest:", largest)
    print("Second Largest:", second_largest)