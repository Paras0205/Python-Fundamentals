# Check whether a list is sorted or not if not sort and then print

my_list=[1,2,5,4,8,3,4,9,0,2]

# if my_list==sorted(my_list):
#     print("list is sorted")
# else:
#     my_list.sort()

# print(my_list)

is_sorted = True

for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("List is already sorted.")
else:
    my_list.sort()
    print("Sorted list:", my_list)