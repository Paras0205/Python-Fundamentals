#Find factorial of a number.
num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print("Factorial of", num, "is:", fact)