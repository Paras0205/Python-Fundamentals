#Operators are symbols used to perform operations on values or variables.

#1. Arithmetic Operators

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor Division
print(a % b)   # Modulus
print(a ** b)  # Exponentiation

# 2. Comparison (Relational) Operators
# Return True or False.
a = 10
b = 20

print(a == b)  # Equal
print(a != b)  # Not Equal
print(a > b)   # Greater Than
print(a < b)   # Less Than
print(a >= b)  # Greater Than Equal To
print(a <= b)  # Less Than Equal To

#3. Logical Operators
a = True
b = False

print(a and b)
print(a or b)
print(not a)

#4. Assignment Operators
x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

#5. Membership Operators
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("grapes" not in fruits)

#6. Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)

print(a is not c)