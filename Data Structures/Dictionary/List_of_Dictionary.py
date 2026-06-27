# A list of dictionaries is just:
    # many records (rows) → stored in a list,
    # each record’s fields (columns) → stored in a dict.

students = [
    {"name": "Aman", "age": 21, "city": "Delhi"},
    {"name": "Ravi", "age": 22, "city": "Mumbai"},
    {"name": "Neha", "age": 23, "city": "Pune"}
]

for s in students:
    print(s["name"], s["city"])

# Common operations:

# 1.Loop through all records:

# for s in students:
#     print(s["name"], s["city"])

# 2.Filter using a condition:

# delhi_students = [s for s in students if s["city"] == "Delhi"]

# 3.Add a new field to each dict:

# for s in students:
#     s["status"] = "active"