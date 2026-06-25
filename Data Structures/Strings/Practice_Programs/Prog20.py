# Remove Spaces from String

s = "data science is fun"

new_s = ""

for char in s:
    if char != " ":
        new_s += char

print(new_s)