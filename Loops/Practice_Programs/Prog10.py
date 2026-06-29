#wap to check prime number in a range and store all prime numbers and not prime numbers in a diff list 
start_range=int(input("enter the start range:"))
end_range=int(input("enter the end range:"))
prime=[]
not_prime=[]
for num in range(start_range,end_range+1):
    if num==1:
        not_prime.append(num)
    elif num>1:
        for i in range(2,num):
            if num%i==0:
                not_prime.append(num)
                break
        else:
            prime.append(num)
print("prime numbers:",prime)
print("not prime numbers:",not_prime)