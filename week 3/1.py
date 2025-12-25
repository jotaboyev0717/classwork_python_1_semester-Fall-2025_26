print("=== Coffee Shop Order System ===")
print("Enter drink sizes: small, medium, or large/nType 'done' when finished ordering")
total = 0
while True:
    a = input("Enter drink size: ")
    if a == "stop":
        break
    elif a == "small":
        total += 3.50
        print("Price: $3.50")
    elif a == "medium":
        total += 4.50
        print("Price: $4.50")
    elif a == "large":
        total += 5.50
        print("Price: $5.50")
    print(f"Current total: {total}")
print("=== Order Summary ===")
print(f"Subtotal: {total}")

if total >= 20:
    print("Loyalty Discount: -$3.00")
    print(f"Final Total: $ {total-3.00}")
print("Thank you for your order!")