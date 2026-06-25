#Check if a string is a palindrome
str=input("Enter a string:")

if str.lower()==str[::-1].lower():
        print("The string is a palindrome")
else:
    print("The string is not a palindrome")