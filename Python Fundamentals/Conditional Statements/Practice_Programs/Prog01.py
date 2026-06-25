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