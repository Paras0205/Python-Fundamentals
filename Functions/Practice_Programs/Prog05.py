# unique_items(lst)
# Input: a list.
# Output: list of unique items.

def unique_items(my_list):
    my_set=set(my_list)
    return list(my_set)

print(unique_items([1,2,3,1,2,5,7,8,8]))