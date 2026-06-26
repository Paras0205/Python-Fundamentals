# Tasks:
# Extract numeric values
# Convert to integers
# Store in new list

prices = ["100", "200", "abc", "300", ""]

new_prices = []
total=0

for p in prices:
    if p.isdigit():
        value=int(p)
        new_prices.append(value)
        total+=value

print("New list:", new_prices)
print("total:",total)