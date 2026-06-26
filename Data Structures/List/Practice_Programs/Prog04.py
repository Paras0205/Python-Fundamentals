# Find the largest number in a list.

my_list=[10,21,34,5,2,67,87,43,99]

# print(f"largest num in a string is: {max(my_list)}")

largest = my_list[0]

for num in my_list:
    if num > largest:
        largest = num

print(f"largest number in a string is:{largest}")