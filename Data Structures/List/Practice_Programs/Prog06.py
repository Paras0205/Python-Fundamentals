# Remove duplicate values from a list.

my_list=[1,2,1,4,5,5,6,4,2,1,8]

value=[]
for num in my_list:
    if num not in value:
        value.append(num)
print(value)