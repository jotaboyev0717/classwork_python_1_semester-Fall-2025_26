print("=== Arcade Game Center Calculator ===")
print("Enter game type: classic, modern, or premium\nType 'done' when finished playing")


total = 0.0
while True:
    type = input("Enter game type: ")
    if type == "done":
        break
    
    if type == "classic":
        price = 2.00
    elif type == "modern":
        price = 4.00
    elif type == "premium":
        price = 6.00
    else:
        print("Invalid membership type. Please enter student, regular, or premium.")
        continue
    
    total += price
    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}")
    
discount = 0.0
if total >= 10:
    discount = 1.50
    
final_disc = total - discount

print("=== Game Summary ===")
print(f"Subtotal: ${total:.2f}")
if discount > 0:
    print(f"Bulk Rental Discount: ${discount:.2f}")
else:
    print("No discount.")
print(f"Final Total: ${final_disc:.2f}")
print("Thank you for your rental!")