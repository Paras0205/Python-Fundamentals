# max_in_list(nums)
# Input: list of integers.
# Output: largest integer.

def max_num(num):

    max_num=num[0]

    for nums in num:
        if nums>max_num:
            max_num=nums
    
    return max_num

my_list=[2,1,5,4,7,5,9,6]

largest_num=max_num(my_list)

print(largest_num)