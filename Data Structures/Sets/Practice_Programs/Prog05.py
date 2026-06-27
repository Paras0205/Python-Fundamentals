# Given two user activity lists (pages visited),
# find: pages visited by both users, pages visited by only one user.

user1 = ["Home", "About", "Products", "Contact", "Blog"]
user2 = ["Home", "Products", "Login", "Blog", "Support"]

user1_set = set(user1)
user2_set = set(user2)

common_pages = user1_set & user2_set
unique_pages = user1_set ^ user2_set

print("Pages visited by both users:")
print(common_pages)

print("\nPages visited by only one user:")
print(unique_pages)