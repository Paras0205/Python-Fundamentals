#Check whether a triangle is valid using three sides.
side1=int(input("enter the first side:"))
side2=int(input("enter the second side:"))
side3=int(input("enter the third side:"))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("triangle is valid")
else:
    print("triangle is not valid")