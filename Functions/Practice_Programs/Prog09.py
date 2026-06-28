#student_result(marks)
# Input: marks (0–100).
# Output: "Pass" or "Fail" (pass if marks ≥ 40).

def stu_result(marks):

    if marks>=40:
        return "Pass"
    else:
        return "Fail"
    
print(stu_result(67))