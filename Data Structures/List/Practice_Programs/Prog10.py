# Split a list into two lists: prime numbers and not prime numbers.

my_list=[1,2,3,4,5,6,7,8,9,10]

prime_num=[]
not_prime_num=[]

for num in my_list:
    if num<=1:
        not_prime_num.append(num)
        continue
    elif num>1:
        for n in range(2,num):
            if num%n==0:
                not_prime_num.append(num)
                break
            else:
                prime_num.append(num)

print("prime numbers:",prime_num)
print("not prime numbers:",not_prime_num)

