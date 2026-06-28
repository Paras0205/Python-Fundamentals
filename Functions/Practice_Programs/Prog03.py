# sum_list(nums)

# Input: list of numbers.

# Output: sum of numbers.

def sum_list(nums):
    total=0
    for num in nums:
        total+=num
    
    return total

my_list=[10,20,20,40,30]

print(sum_list(my_list))