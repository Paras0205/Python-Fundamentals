# Count how many even numbers are in a list

my_list=[1,2,3,4,5,6,7,8,9,10]
count=0

for num in my_list:
    if num%2==0:
        count+=1
print(f"count of even number in a list is:{count}")