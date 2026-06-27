Student={}

while True:
    print("Student Report Management System:")
    print("1. Add student")
    print("2. Update student")
    print("3. Delete student")
    print("4. View student report")
    print("5. View all student report")
    print("6. Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        roll=int(input("Enter the student roll number:"))
        if roll in Student:
            print("Student already exist.")
        else:
            name=input("Enter name of a student:").title()
            marks=float(input("Enter marks of a student:"))
            Student[roll]={
                "name":name,
                "marks":marks
            }
            print("Student added successfully.")
    
    elif choice=="2":
        roll=int(input("Enter the student roll number:"))
        if roll in Student:
            new_marks=float(input("Enter updated marks of a student:"))
            Student[roll]["marks"]=new_marks
            print("Student marks updated successfully.")
        else:
            print("Student not exist.")

    elif choice=="3":
        roll=int(input("Enter the student roll number:"))
        if roll in Student:
            Student.pop(roll)
            print("Student deleted successfully.")
        else:
            print("Student not exist.")

    elif choice=="4":
        roll=int(input("Enter the student roll number:"))
        if roll in Student:
            name=Student[roll]["name"]
            marks=Student[roll]["marks"]

            if marks>90:
                grade="A"
            elif marks >= 80:
                grade = "B"

            elif marks >= 70:
                grade = "C"

            elif marks >= 60:
                grade = "D"

            else:
                grade = "Fail"
            
            print("Roll No :", roll)
            print("Name    :", name)
            print("Marks   :", marks)
            print("Grade   :", grade)

        else:
            print("Student Not Found.")

    elif choice=="5":
        if len(Student)==0:
            print("No student record found.")
        else:
            print(f"{'Roll Number':<20}{'Name':<20}{'Marks':<10}{'Grade':<10}")

            for roll, details in Student.items():
                marks = details["marks"]
                if marks >= 90:
                    grade = "A"
                elif marks >= 80:
                    grade = "B"
                elif marks >= 70:
                    grade = "C"
                elif marks >= 60:
                    grade = "D"
                else:
                    grade = "Fail"
                print(f"{roll:<20}{details['name']:<20}{marks:<10}{grade:<10}")

    elif choice=="6":
         print("Thank You!")
         break

    else:
        print("Invalid Choice.")