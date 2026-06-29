# WAP TO PRINT ALL PRIME NO IN AN INTERVAL
lower_num=int(input("enter the lower number:"))
upper_num=int(input("enter the upper number:"))
for num in range(lower_num,upper_num+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print("prime:",num)