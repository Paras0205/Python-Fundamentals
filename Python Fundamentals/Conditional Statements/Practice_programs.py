#WAP to create a dynamic calculator
while True:
    operator=input("enter the operator:")
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    if operator=="+":
        sum=num1+num2
        print("sum is:",sum)
    elif operator=="-":
        sub=num1-num2
        print("subtraction is:",sub)
    elif operator=="*":
        mul=num1*num2
        print("multiplication is:",mul)
    elif operator=="/":
        if num2!=0:
            div=num1/num2
            print("division is:",div)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator.")

    continue_calculation=input("Do you want to perform another calculation? (yes/no): ")
    if continue_calculation.lower() != "yes":
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Starting a new calculation...")

# Wap to find out whether a student has passed or failed if it requires a total of 40% .
# Assume 3 subjects and take marks as an input from the user

sub1=int(input("enter the marks of subject 1:"))
sub2=int(input("enter the marks of subject 2:"))
sub3=int(input("enter the marks of subject 3:"))
total_marks=sub1+sub2+sub3
percentage=(total_marks/300)*100
if percentage>=40:
    print("student has passed")
else:
    print("student has failed")

# WAP TO CHECK WHETHER A NO IS +,-,0
num=int(input("enter the number:"))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")

# If username correct
# Then check password
# Print login success or failure
username=input("enter the username:")
password=input("enter the password:")
if username=="Paras":
    if password=="1234":
        print("login success")
    else:
        print("login failure")

#Find the largest of three numbers.
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if num1>num2 and num1>num3:
    print("largest number is:",num1)
elif num2>num1 and num2>num3:
    print("largest number is:",num2) 
else:
    print("largest number is:",num3)

#Check whether a number is divisible by 3 and 5.
num=int(input("enter the number:"))
if num%3==0 and num%5==0:
    print("number is divisible by 3 and 5")
else:
    print("number is not divisible by 3 and 5")


#WAP to check whether a year is a leap year or not.
year=int(input("enter the year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("year is a leap year")
else:
    print("year is not a leap year")

#Check whether a triangle is valid using three sides.
side1=int(input("enter the first side:"))
side2=int(input("enter the second side:"))
side3=int(input("enter the third side:"))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("triangle is valid")
else:
    print("triangle is not valid")

#Create a tax calculator using income slabs.
income=float(input("enter your income:"))
if income<=250000:
    tax=0
elif income<=500000:
    tax=income*0.1
elif income<=1000000:
    tax=income*0.2
else:
    tax=income*0.3
print("tax to be paid:",tax)

#Build an ATM withdrawal checker based on balance and withdrawal amount.
balance=float(input("enter your balance:"))
withdrawal=float(input("enter the withdrawal amount:"))
if withdrawal <= balance:
    print("withdrawal successful")
    print("remaining balance:", balance - withdrawal)
else:
    print("insufficient balance")