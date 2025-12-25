def calculate_item_total(quantity, unit_price):
    return quantity * unit_price

def apply_bulk_discount(total, quantity):
    if quantity >=10:
        return total * 0.10
    elif quantity >= 5:
        return total * 0.05
    else:
        return 0
    
def calculate_tax(subtotal, tax_rate):
    return subtotal * (tax_rate / 100)

def is_eligible_for_free_shipping(subtotal):
    return subtotal >= 50

def process_order(item_name, quantity, unit_price, tax_rate):
    print(f"Order receipt for: {item_name}")
    print(f"    Quantity: {quantity} @ ${unit_price:.2f} each")
    
    item_total = calculate_item_total(quantity, unit_price)
    print(f"    Item Total: ${item_total:.2f}")
    
    discount = apply_bulk_discount(item_total, quantity)
    if discount > 0:
        print(f"    Bulk discount: -${discount:.2f}")
    else:
        print(f"    Bulk discount: $0.00")
    
    subtotal = item_total - discount
    print(f"    Subtotal: ${subtotal:.2f}")
    
    tax = calculate_tax(subtotal, tax_rate)
    print(f"    Tax ({tax_rate}%): ${tax:.2f}")
    
    if is_eligible_for_free_shipping(subtotal):
        print(" Eligible for free shipping")
    else:
        remaining = 50 -subtotal
        print(f"    NEED ${remaining:.2f} more for free shipping")
    print("----------------------------------------")

print("SHOPPING CART CALCULATOR")
print("========================================")

process_order("Notebooks", 12, 3.50, 8)
process_order("Pens", 6, 1.25, 8)
process_order("Paper", 3, 4.99, 8)