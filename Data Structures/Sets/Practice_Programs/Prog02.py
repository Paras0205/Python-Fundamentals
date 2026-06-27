# Check if a given value appears in a list using a set

my_list = [1,2,3,4,5,6,7,2,1,3]

my_set = set(my_list)

value = int(input("Enter value to check: "))

print(value in my_set)