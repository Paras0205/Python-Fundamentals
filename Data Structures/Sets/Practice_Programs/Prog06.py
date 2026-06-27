# Given a list of email IDs, find how many unique domains (gmail.com, yahoo.com, etc.) exist:
# Extract domain part.
# Use a set to store domains.

emails = [
    "paras@gmail.com",
    "rahul@yahoo.com",
    "amit@gmail.com",
    "rohit@outlook.com",
    "sonu@yahoo.com",
    "alice@hotmail.com"
]

domains = set()

for email in emails:

    parts = email.split("@")

    domain = parts[1]

    domains.add(domain)

print("Unique Domains:")
print(domains)

print("Total Unique Domains:", len(domains))