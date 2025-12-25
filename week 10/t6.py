users = {
    "Alice": ["Coding", "Music", "Hiking", "Pizza"],
    "Bob":   ["Movies", "Hiking", "Tacos"],
    "Charlie": ["Coding", "Pizza", "Gaming", "Music"],
    "David": ["Cooking", "Travel"]
}

target = "Alice"
target_interests = users[target]

first_person = True

for person, interests in users.items():
    if person == target:
        continue

    shared = 0
    for item in interests:
        if item in target_interests:
            shared += 1

    print(f"Comparing {target} with {person}... {shared} shared interests.")

    if first_person:
        best_friend = person
        best_score = shared
        first_person = False
    else:
        if shared > best_score:
            best_friend = person
            best_score = shared

print("------------------------------")
print(f"Best match for {target} is {best_friend} with {best_score} shared interests.")
