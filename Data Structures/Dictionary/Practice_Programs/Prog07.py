#Given a list of transactions (user, amount), build a dict of total amount per user

transactions = [
    ("Paras", 500),
    ("Rahul", 300),
    ("Paras", 200),
    ("Amit", 700),
    ("Rahul", 100)
]

total = {}

for user, amount in transactions:
    total[user] = total.get(user, 0) + amount

print(total)