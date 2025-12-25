data = """  john smith - 1990
SARAH CONNOR - 1984
  kylo REN - 1995
LARA croft - 1992"""

with open("raw_users.txt", "w") as f:
    f.write(data)

with open("raw_users.txt", "r") as f:
    lines = f.readlines()

with open("clean_profiles.txt", "w") as f:
    for line in lines:
        line = line.strip()
        if line:
            full = line.split("-")
            name = full[0].strip().title()
            year = 2025 - int(full[1].strip())
            f.write(f"Name: {name} (Age: {year})\n")