# Given a dict of {product: price}, find the most expensive product.

products = {
    "Laptop": 65000,
    "Mobile": 25000,
    "Headphones": 3000,
    "Monitor": 18000
}

max_product=""
max_price=0

for product,price in products.items():
    if price>max_price:
        max_price=price
        max_product=product

print("Most expensive product:", max_product)
print("Price:", max_price)