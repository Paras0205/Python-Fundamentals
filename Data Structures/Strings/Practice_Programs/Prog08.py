#Remove all duplicate characters from a string (keep first occurrence).

str=input("Enter a string:")
result = ""

for char in str:
    if char not in result:
        result+=char
print("String after removing duplicates:", result)