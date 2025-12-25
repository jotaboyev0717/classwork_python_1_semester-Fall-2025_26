# File 1: Words to ignore
stops = """the
is
at
on
a
and"""

with open("stopwords.txt", "w") as f:
    f.write(stops)

# File 2: The text to analyze
story = """The cat sat on the mat. 
The cat is a good cat. 
Is the dog on the mat? No, the dog is at the park."""

with open("stopwords.txt") as f:
    stops = []
    for w in f:
        w = w.strip() 
        w = w.lower()
        stops.append(w)


with open("story.txt") as f:
    words = f.read().lower().split()

freq = {}

for w in words:
    w = w.strip(".,?")
    if w != "" and w not in stops:
        freq[w] = freq.get(w, 0) + 1

with open("analysis.txt", "w") as f:
    f.write("WORD FREQUENCY REPORT\n")
    f.write("---------------------\n")
    for k, v in freq.items():
        f.write(f"{k}: {v}\n")
