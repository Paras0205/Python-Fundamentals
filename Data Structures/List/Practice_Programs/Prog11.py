# Find the most frequent number in a list.

my_list=[1,2,3,4,4,6,7,2,3,8]

# freq={}

# max_num=None
# max_count=0

# for num in my_list:
#     freq[num]=freq.get(num,0)+1

# for num,count in freq.items():
#     if count>max_count:
#         max_count = count
#         max_num = num

# print(max_num, max_count)

my_list = [1,2,3,4,4,6,7,2,3,8]

freq = {}

for num in my_list:
    freq[num] = freq.get(num, 0) + 1

max_count = max(freq.values())

print("Most frequent numbers:")

for num, count in freq.items():
    if count == max_count:
        print(num, "->", count)