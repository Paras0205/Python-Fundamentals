#Find nth Fibonacci Number
n = int(input("Enter the position of Fibonacci number: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\nThe", n, "th Fibonacci number is:", a)