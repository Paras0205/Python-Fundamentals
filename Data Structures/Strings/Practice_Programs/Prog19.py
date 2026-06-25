#WAP to find first non repeating character in a string

str=input("enter a string:")
char_count={}

for char in str:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1

for i in range(len(str)):
    if char_count[str[i]]==1:
        print("first non repeating char:",str[i])
        break


