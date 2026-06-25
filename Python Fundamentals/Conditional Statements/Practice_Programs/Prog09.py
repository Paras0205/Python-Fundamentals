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