# Create a dictionary for your profile: name, age, city, role.
# Access and print only the name and city.
# Add a new key "skills" with a list of skills.
# Remove the "age" key.

profile={
    "name":"Paras",
    "age":21,
    "city":"Ganaur",
    "role":"Data analyst"
}

print("Name:", profile["name"])
print("City:", profile["city"])

profile["skills"] = ["Python", "SQL", "Excel", "Power BI"]

profile.pop("age")

print(profile)