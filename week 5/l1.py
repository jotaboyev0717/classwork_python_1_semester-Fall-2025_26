guests = ["Alice", "Bob", "Charlie"]
print(f"Initial guests: {guests}")

# A new guest, "David", confirms. Add him to the end.
guests.append("David")
print(f"After adding David: {guests}")

# A VIP guest, "Eve", needs to be at the start of the list (index 0).
guests.insert(0, "Eve")
print(f"After adding VIP Eve: {guests}")

# "Bob" cancels. Remove him by his name.
guests.remove("Bob")
print(f"After Bob cancels: {guests}")

# The last person to arrive has to leave.
guests.pop() # .pop() with no argument removes the last item
print(f"After the last person leaves: {guests}")
    
# We misspelled "Alice". Let's correct it by changing the value at index 1.
guests[1] = "Alicia" # The first guest 'Eve' is at index 0
print(f"After correcting a name: {guests}")