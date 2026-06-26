# Merge two lists without duplicates.

list_1=[1,2,3,4,5,6,7,8]
list_2=[5,6,7,8,9,0,11,-1]

# merged = list(set(list_1 + list_2))           #method1
# print(merged)

merged_list=[]

# for num in list_1:                            #method2
#     if num not in merged_list:
#         merged_list.append(num)
    
# for num in list_2:
#     if num not in merged_list:
#         merged_list.append(num)

# merged_list.sort()
# print("merged_list:",merged_list)

merged_list=list_1.copy()                       #method3

for num in list_2:
    if num not in merged_list:
        merged_list.append(num)

merged_list.sort()

print(merged_list)