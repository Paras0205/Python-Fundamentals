#WAP TO COUNT VOWELS AND CONSONANT IN A STRING
str=input("enter the string:")
vowel=0
consonent=0
for char in str:
    if char in "aeiouAEIOU":
        vowel+=1
    elif(char==" "):
        continue
    elif char.isalpha():
        consonent+=1
print("Number of vowels:", vowel)
print("Number of consonants:", consonent)