products = {
    "101": ("Milk", 2.50),
    "102": ("Eggs", 3.00),
    "103": ("Bread", 1.75),
    "104": ("Cheese", 4.50),
    "105": ("Apple", 0.50)
}

cart = ["101", "105", "105", "999", "103", "105"]
total = 0
for i in cart:
    if i in products:
        name, price = products[i]
        print(f"{name}: {price}")
        total += price  
    else:
        print(f"item {i} not found")
print(total)