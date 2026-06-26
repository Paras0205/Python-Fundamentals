# Tasks:
# Print all numbers
# Find total
# Find average

my_list=[1,2,3,6,5,7,8,10,-1]

total=0

for num in my_list:
    print(num,end=" ")
    total+=num

average=total/len(my_list)

print(f"\ntotal is: {total}")
print(f"average is: {average}")