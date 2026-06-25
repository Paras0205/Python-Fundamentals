#Check if a string starts with "www" and ends with ".com"

website = input("Enter website: ")

if website.startswith("www") and website.endswith(".com"):
    print("Valid website")
else:
    print("Invalid website")