data = """Lunch,12.50
Coffee,5.00
Office Supplies,23.75
Taxi,10.00
Coffee,8.25
Dinner,50.00"""

with open("expenses.txt", "w") as f:
    f.write(data)

with open("expenses.txt", "r") as f:
    lines = f.readlines()

total = 0
count = 0

for line in lines:
    line = line.strip()
    if line:
        parts = line.split(",")
        amount = float(parts[1])
        total += amount
        count += 1

average = total / count 
if count != 0:
    average = total / count
else:
    average = 0

print("--- Expense Report ---")
print(f"Total Transactions: {count}")
print(f"Total Spent: ${total:.2f}")
print(f"Average Expense: ${average:.2f}")
