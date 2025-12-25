data = """1001:Alice
1002:Bob
1003:Alice
ERROR_READING_LINE
1004: Charlie
1005:Alice
1006:Bob
1007:   
1008:David"""

with open("votes.txt", "w") as f:
    f.write(data)

with open("votes.txt", "r") as f:
    lines = f.readlines()

votes = {}   

for line in lines:
    line = line.strip()
    if not line:
        continue

    parts = line.split(":")
    if len(parts) != 2:
        continue

    name = parts[1].strip()
    if not name:
        continue

    votes[name] = votes.get(name, 0) + 1

total = sum(votes.values())

with open("results.txt", "w") as f:
    f.write("OFFICIAL ELECTION RESULTS\n")
    f.write("-------------------------\n")

    for name, count in votes.items():
        percent = count / total * 100
        f.write(f"{name}: {count} votes ({percent:.1f}%)\n")

    f.write("\n-------------------------\n")
    f.write(f"Total Valid Votes: {total}\n")

    winner = max(votes, key=votes.get)
    f.write(f"WINNER: {winner}\n")

