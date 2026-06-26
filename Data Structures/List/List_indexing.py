marks = [85, 92, 78, 90, 88]

# Access by index
print(marks[0])          # 85  (first)
print(marks[-1])         # 88  (last)
print(marks[1:3])        # [92, 78]  (slicing)

# Modify
marks[0] = 95            # change first element

# Useful built-ins
print(len(marks))        # 5
print(sum(marks))        # 433
print(min(marks))        # 78
print(max(marks))        # 92
print(sorted(marks))     # [78, 85, 88, 90, 92]