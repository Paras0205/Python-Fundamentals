#Print numbers from 1 to 10.
for i in range(1, 11):
    print(i,end=" ")

#Print all even numbers from 1 to 20.
for i in range(1, 21):
    if i%2==0:
        print(i,end=" ")

#Print each character of a string.
str=input("enter the string:")
for char in str:
    print(char,end=" ")

#Find the sum of first 10 natural numbers.
sum=0
for i in range(1, 11):
    sum+=i
print("Sum of first 10 natural numbers:", sum)

#Count how many vowels are in a string.
str=input("enter the string:")
vowel=0
for char in str:
    if char in "aeiouAEIOU":
        vowel+=1
print("Number of vowels in the string:", vowel)

#Print multiplication table of a number.
num=int(input("enter the number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#Find factorial of a number.
num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print("Factorial of", num, "is:", fact)

#Check whether a number is prime or not.
num=int(input("enter the number:"))
if num==1:
    print("num is not prime num")
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")

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
            
#WAP TO COUNT VOWELS AND CONSONANT IN A STRING
str=input("enter the string:")
vowel=0
consonent=0
for char in str:
    if char in "aeiouAEIOU":
        vowel+=1
    elif(char==" "):
        continue
    elif char.isalpha():
        consonent+=1
print("Number of vowels:", vowel)
print("Number of consonants:", consonent)

# Keep taking input from user until they enter 0.
# Then print total and average.
total = 0
count = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    total += num
    count += 1
if count > 0:
    average = total / count
    print("Total:", total)
    print("Average:", average)
else:
    print("No numbers entered.")

# Reverse a number
num = int(input("Enter a number: "))
rev=""
for i in range(num):
    rev=i+rev
print("Reverse of the number is:",rev)

#rev a number using while loop
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reverse of the number is:", rev)

#Find nth Fibonacci Number
n = int(input("Enter the position of Fibonacci number: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("The", n, "th Fibonacci number is:", a)

#Factorial of a number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)