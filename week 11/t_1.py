def sum_valid_prices(price_list):
    total = 0
    for item in price_list:
        if item == "Free":
            price = 0.0
        elif "$" in item:
            item = item.strip("$")
            price = float(item)
        else:    
            try:
                price = float(item) 
            except ValueError:
                print(f"Skipping invalid data: {item}")
                continue
        total += price
    return total  
raw_prices = ["$12.50", "Free", "error_404", "$5.00", "2.50", "N/A"]
total = sum_valid_prices(raw_prices)
print(f"Total: ${total}")