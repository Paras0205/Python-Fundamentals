# A dictionary where one of the values is itself another dictionary

students = {
    101: {"name": "Paras", "marks": 95},
    102: {"name": "Ravi", "marks": 88},
    103: {"name": "Neha", "marks": 92}
}

# print(students.items())
print(students[101]["marks"])
print(students[103]["name"])

for emp_id, info in students.items():
    print(emp_id, info["name"], info["marks"])
