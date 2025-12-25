# Format: Product, Stock, Minimum
data = """Apples,50,100
Bananas,120,100
Cherries,5,20
Dates,50,50
Eggs,10,24"""

with open("inventory.csv", "w") as f:
    f.write(data)
    
with open("inventory.csv", "r") as f:
    lines = f.readlines()
    
with open("reorder_list.txt", "w") as f:
    for line in lines:
        line = line.strip()
        if line:
            part = line.split("")
            item = part[0]
            amount_have = int(part[1])
            amount_need = int(part[2])
            need = amount_have - amount_need
            if need < 0:
                f.write(f"Item: {item} | Order amount: {-need}\n")