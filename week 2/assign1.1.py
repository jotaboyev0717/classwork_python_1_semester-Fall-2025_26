item1 = input("1st item: ")
price1 = input("1st item price: ")
quantity1 = int(input("1st item quantity: "))

item2 = input("2nd item: ")
price2 = input("2nd item price: ")
quantity2 = int(input("2nd item quantity: "))

item3 = input("3rd item: ")
price3 = input("3rd item price: ")
quantity3 = int(input("3rd item quantity: "))

name = input("What's your name: ")
is_member_input = input("is_member (yes or no): ")
is_member = True if is_member_input == "yes" else False
total_previous_purchases =  float(input("Enter previous purchases in sum: "))

subtotal = float(price1 * quantity1 + price2 * quantity2 + price3 * quantity3)
quantity = quantity1 + quantity2 + quantity3

member_discount = 0.1 * subtotal * is_member

bulk_discount = 0.05 * subtotal * (quantity > 5)

loyalty_discount = 0.03 * subtotal * (total_previous_purchases >= 1000000)

overall = member_discount + bulk_discount + loyalty_discount

total = 0.12 * overall

shipping = (subtotal <= 500000) * 25000

print(f"Customer name: {name}")
print(f"{item1}: {price1} * {quantity1} = {price1 * quantity1}")
print(f"{item2}: {price2} * {quantity2} = {price2 * quantity2}")
print(f"{item3}: {price3} * {quantity3} = {price3 * quantity3}")
print(f"Subtotal: {subtotal}")
print(f"")