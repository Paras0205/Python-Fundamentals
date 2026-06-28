# filter_even_odd(nums)
# Input: list of integers.
# Output: list of only even and odd numbers.

def even_odd(nums):

    even_num=[]
    odd_num=[]

    for num in nums:
        if num%2==0:
            even_num.append(num)
        else:
            odd_num.append(num)

    return even_num,odd_num

my_list=[1,2,3,4,5,6,7,8,9,10]

even,odd=even_odd(my_list)

print("Even numbers:",even)
print("Odd numbers:",odd)