# 1. `keys()`, `values()`, `items()`

# Given:

student = {"name": "Aman", "age": 21, "city": "Delhi"}
student.keys()          #all keys.
student.values()        #all values.
student.items()         #key–value pairs.

# Example:

print(student.keys())      # dict_keys(['name', 'age', 'city'])
print(student.values())    # dict_values(['Aman', 21, 'Delhi'])

for key, value in student.items():
    print(key, "->", value)

# When to use:
    # Looping through a dictionary.
    # Inspecting all keys/values.
    # Building new structures from dict data. 

# 2. get()   Safe way to read a value.

student = {"name": "Aman", "age": 21}

print(student.get("name"))              # 'Aman'
print(student.get("city"))              # None
print(student.get("city", "Unknown"))   # 'Unknown'

# Why useful:
    # Avoids errors when the key might be missing.
    # Very important in counting and aggregation.

# Pattern for counting:

freq = {}
for ch in "data":
    freq[ch] = freq.get(ch, 0) + 1

#3.update()   Merge another dictionary or key–value pairs into this dict.

student = {"name": "Aman", "age": 21}
student.update({"city": "Delhi", "age": 22})
print(student)  # {'name': 'Aman', 'age': 22, 'city': 'Delhi'}

# Notes:
    # Existing keys get overwritten.
    # New keys are added.

# 4. pop() and popitem()

# pop(key, default)
# Remove a specific key and return its value.

student = {"name": "Aman", "age": 21}
age = student.pop("age")         # age = 21, dict loses 'age'
age2 = student.pop("height", 0)  # returns 0 instead of error

#popitem()
# Remove and return the last inserted key–value pair as a tuple.

student = {"name": "Aman", "age": 21}
item = student.popitem()   # e.g. ('age', 21)

# 5. setdefault()       Get a key’s value, or if it doesn’t exist, create it with a default.

student = {"name": "Aman"}
val1 = student.setdefault("name", "Unknown")   # 'Aman', dict unchanged
val2 = student.setdefault("city", "Delhi")    # 'Delhi', adds 'city' key

# Great for:
    # Building dictionaries of lists or counts.
    # Grouping data.

# Example: grouping by first letter:

words = ["apple", "ant", "ball"]
groups = {}

for w in words:
    key = w[0]
    groups.setdefault(key, []).append(w)

print(groups)  # {'a': ['apple', 'ant'], 'b': ['ball']}

#6. clear() and copy()

student = {"name": "Aman", "age": 21}

clone = student.copy()   # shallow copy
student.clear()          # now student is {}

# Use:
    # copy() when you want a separate copy to modify.
    # clear() when you want to empty the dictionary quickly. 


## 7. fromkeys()    Create a new dict from a list of keys.

keys = ["math", "science", "english"]
marks = dict.fromkeys(keys, 0)
print(marks)  # {'math': 0, 'science': 0, 'english': 0}

# Useful for initializing structures.

## Summary of the most used methods

# | Method        | What it does                                       |
# |--------------|-----------------------------------------------------|
# | `keys()`     | View of all keys                                   |
# | `values()`   | View of all values                                 |
# | `items()`    | View of all (key, value) pairs                     |
# | `get()`      | Safe read with default                             |
# | `update()`   | Merge / overwrite with another dict                |
# | `pop()`      | Remove key and return its value                    |
# | `popitem()`  | Remove last key–value pair and return it           |
# | `setdefault()`| Get or create key with default value              |
# | `clear()`    | Remove all items                                   |
# | `copy()`     | Shallow copy of dict                               |
# | `fromkeys()` | New dict from iterable of keys with one default    | 
