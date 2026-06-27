# Dictionary is a collection of keys-value pairs.

# PROPERTIES OF PYTHON DICTIONARIES 
    # Keys are like labels (must be immutable: strings, numbers, tuples)
    # Values can be anything (string, number, list, another dict, etc.).
    # Each key is unique; values may repeat.
    # You access data by key, not by index.
    
student = {
    "name"  : "Paras",
    "branch": "AI & DS",
    "cgpa"  : 8.5,
    "placed": False
}

# Access value by key
print(student["name"])          # Paras
print(student["cgpa"])          # 8.5

# Safe access — no error if key missing
print(student.get("age"))       # None
print(student.get("age", 21))   # 21 (default value)

# Add / update
student["year"] = 4             # adds new key
student["cgpa"] = 8.7           # updates existing key

# Delete
del student["placed"]           # removes key