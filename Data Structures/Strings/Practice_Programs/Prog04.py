#WAP TO COUNT THE NUMBER OF DIGITS, LETTERS AND SPACES IN A STRING
digit=0
letters=0
spaces=0
str=input("Enter a string:")
for char in str:
    if char.isdigit():
        digit += 1
    elif char.isalpha():
        letters += 1
    elif char.isspace():
        spaces += 1
print("Digits:", digit)
print("Letters:", letters)
print("Spaces:", spaces)