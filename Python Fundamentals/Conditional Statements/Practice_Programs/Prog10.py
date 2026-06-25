#Build an ATM withdrawal checker based on balance and withdrawal amount.
balance=float(input("enter your balance:"))
withdrawal=float(input("enter the withdrawal amount:"))
if withdrawal <= balance:
    print("withdrawal successful")
    print("remaining balance:", balance - withdrawal)
else:
    print("insufficient balance")