student = {"name":"Paras","branch":"AI & DS","cgpa":8.5}

# Loop keys only
for key in student:
    print(key)

# Loop values only
for value in student.values():
    print(value)

# Loop both — most useful
for key, value in student.items():
    print(f"{key}: {value}")

# Always use .items() when we need both key and value.