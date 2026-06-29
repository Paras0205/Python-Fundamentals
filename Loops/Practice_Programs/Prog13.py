# Reverse a number
num = int(input("Enter a number: "))
rev=""
for i in range(num):
    rev=i+rev
print("Reverse of the number is:",rev)