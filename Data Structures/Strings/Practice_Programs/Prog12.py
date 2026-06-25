#Mask a phone number, showing only last 4 digits:

phone = "9876543210"

masked = "*" * 6 + phone[-4:]

print(masked)