#calculator

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "Invalid number"
    return a/b

operations={
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division
}

while True:
    operator=input("Enter the operator:")

    if operator not in operations:
        print("Invalid operator.")
        continue

    num1=float(input("Enter the num 1:"))
    num2=float(input("Enter the num 2:"))

    result=operations[operator](num1,num2)

    print(result)

    choice=input("Want to continue calculation (Yes/No):").lower()
    if choice!="Yes":
        print("End of calculations")
        break
