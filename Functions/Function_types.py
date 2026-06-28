# Type 1 — No parameter, no return (just prints)
def greet():
    print("Hello! Welcome to Data Analysis.")

greet()   # Hello! Welcome to Data Analysis.
greet()   # call it as many times as you want

# Type 2 — With parameters, no return
def greet_student(name, course):
    print(f"Welcome {name}! You are enrolled in {course}.")

greet_student("Paras", "Data Science")
greet_student("Rahul", "Data Analytics")

# Type 3 — With parameters AND return
def calculate_percentage(marks, total=100):
    percentage = (marks / total) * 100
    return percentage

p1 = calculate_percentage(85)        # 85.0
p2 = calculate_percentage(45, 60)    # 75.0
print(f"Student 1: {p1:.1f}%")
print(f"Student 2: {p2:.1f}%")

# Type 4 — Default parameters
# passing_mark has a default value of 50
def check_result(marks, passing_mark=50):
    if marks >= passing_mark:
        return "Pass"
    return "Fail"

print(check_result(75))        # Pass (uses default 50)
print(check_result(75, 80))    # Fail (overrides default)
print(check_result(45))        # Fail

# Type 5 — Returning multiple values
def analyse_marks(marks):
    avg     = sum(marks) / len(marks)
    highest = max(marks)
    lowest  = min(marks)
    passed  = len([m for m in marks if m >= 50])
    return avg, highest, lowest, passed

# Unpack all return values
avg, high, low, passed = analyse_marks([85, 42, 91, 55, 38, 76])
print(f"Average : {avg:.1f}")
print(f"Highest : {high}")
print(f"Lowest  : {low}")
print(f"Passed  : {passed}")