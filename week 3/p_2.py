total = 0
while True:
    answer = input("Enter a number 'done': ")
    if answer == "done":
        break
    answer = float(answer)
    total += answer
    print(f"Current total: {total}")
print(f"Current total: {total}")