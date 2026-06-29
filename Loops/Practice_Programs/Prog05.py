#Count how many vowels are in a string.
str=input("enter the string:")
vowel=0
for char in str:
    if char in "aeiouAEIOU":
        vowel+=1
print("Number of vowels in the string:", vowel)