# Read a given string, change the character at a given index and then print the modified string.

s = input("enter the string:")
index = int(input("enter the index:"))
new_char = input("enter the new character:")

result = ""

for i in range(len(s)):
    if i == index:
        result += new_char
    else:
        result += s[i]

print(result)