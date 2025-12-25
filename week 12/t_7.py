store_a = """Laptop,5,999.99
Mouse,20,25.00
Keyboard,15,75.00
Monitor,8,300.00"""

store_b = """Laptop,3,999.99
Mouse,35,25.00
Headphones,12,150.00
Keyboard,10,75.00"""

store_c = """Mouse,25,25.00
Monitor,5,300.00
Headphones,8,150.00
Laptop,7,999.99"""

with open("store_a.csv", "w") as f:
    f.write(store_a)

with open("store_b.csv", "w") as f:
    f.write(store_b)

with open("store_c.csv", "w") as f:
    f.write(store_c)
    
with open("store_a.csv") as f:
    a = []
    for i in f:
        a.append(i.strip("\n").split(","))
        
with open("store_a.csv") as f:
    b = []
    for i in f:
        b.append(i)

with open("store_a.csv") as f:
    c = []
    for i in f:
        c.append(i)
name = a[0]
quantity = a[1]
price = a[2]
print(name)