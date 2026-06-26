# Split a list into two lists: even numbers and odd numbers.

my_list=[1,2,4,6,7,32,7,8,7,5,9,21,55,2]
even_num=[]
odd_num=[]

for num in my_list:
    if num%2==0:
        if num not in even_num:
            even_num.append(num)
            even_num.sort()
    else:
        if num not in odd_num:
            odd_num.append(num)
            odd_num.sort()

print("even number:",even_num)
print("odd number:",odd_num)