def checkout(inventory, cart):
    total_cost = 0.0
    failed = 0
    for item in cart:
        try:
            value = inventory[item]
            if value == None:
                raise TypeError("Price missing")
            if value < 0:
                raise ValueError("Invalid Price")
            total_cost += value
        except KeyError:
            print(f"Item not found: {item}")
            failed += 1
        except (TypeError , ValueError) as e:
            print(f"Data error for {item}: {e}")
            failed += 1
    return (total_cost, failed)
store_db = {
    "Apple": 0.50, 
    "Banana": 0.30, 
    "GhostItem": None,     # Corrupt data
    "GlitchItem": -5.00    # Corrupt data
}
my_cart = ["Apple", "Mango", "GhostItem", "Banana", "GlitchItem"]

cost, errors = checkout(store_db, my_cart)
print(f"Total: ${cost}, Errors: {errors}")