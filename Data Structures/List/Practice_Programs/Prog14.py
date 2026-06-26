# Tasks:
#     Ignore zeros
#     Count positives
#     Count negatives
#     Create two lists:
#         positives
#         negatives

my_list=[1,2,3,-1,-2,10,0,0,00,-7,8,-0,9,-6]

posi_num=[]
nega_num=[]

for num in my_list:
    if num==0:
        continue
    elif num>0:
        posi_num.append(num)
    else:
        nega_num.append(num)

print("positive numbers:",posi_num)
print("total positive numbers in a list are:",len(posi_num))
print("negative numbers:",nega_num)
print("total negative numbers in a list are:",len(nega_num))