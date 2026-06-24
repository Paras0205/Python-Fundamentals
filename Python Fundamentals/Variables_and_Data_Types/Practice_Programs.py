#Store your name, age, and city in variables
Name="Paras"
Age=21
City="Ganaur"
print("My name is", Name, "I am", Age, "years old and I live in", City)

#wap to add 2 numbers
a=2
b=3
sum=a+b
print(sum)
print(a+b)

#Take student details and print a formatted profile.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
college = input("Enter your college name: ")
city = input("Enter your city: ")

print("\n----- Student Profile -----")
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("College:", college)
print("City:", city)

# WAP TO FIND AREA OF TRIANGLE
base=int(input("enter the base of triangle:"))
height=int(input("enter the height of triangle:"))
area=(1/2)*base*height
print("area of triangle:",area)

# WAP TO SWAP TWO VARIABLES  (using 3rd variable)
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
temp=0
temp=a
a=b
b=temp
print("after swapping a:",a)
print("after swapping b:",b)

#WAP TO SWAP TWO VARIABLES (without using 3rd variable)
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
a,b=b,a
print("after swapping a:",a)
print("after swapping b:",b)

#WAP TO FIND SIMPLE INTEREST
p=float(input("enter principle:"))
r=float(input("enter rate:"))
t=float(input("enter time:"))
SI=(p*r*t)/100
print("simple interest is:",SI)

#Store price and quantity → calculate total bill.
price=int(input("enter the price:"))
quantity=int(input("enter the quantity:"))
total_bill=price*quantity
print("total bill:",total_bill)

#WAP TO FIND AREA OF CIRCLE
radius=float(input("enter the radius of circle:"))
area=3.14*radius**2
print("area of circle:",area)

