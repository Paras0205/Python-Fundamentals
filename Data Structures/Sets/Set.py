# A set is a collection of unique, unordered items.
#A set automatically removes duplicates. Use it when we only care about unique values, not order or count.

# Key properties:
    # No duplicates.
    # Unordered (no fixed position, no indexing).
    # Mutable as a container (you can add/remove items), but individual items inside must be immutable.

cities = ["Delhi","Mumbai","Delhi","Pune","Mumbai","Delhi"]

# Convert list to set — removes duplicates instantly
unique = set(cities)
print(unique)           # {'Mumbai', 'Pune', 'Delhi'} (order random)
print(len(unique))      # 3

# Create set directly
skills = {"Python","SQL","Power BI","Python"}
print(skills)           # {'Python', 'SQL', 'Power BI'}

# Add / remove
skills.add("Excel")
skills.discard("SQL")   # no error if missing

# Membership check — sets are FAST at this
print("Python" in skills)   # True