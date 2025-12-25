codon_table = {
    "ATG": "Methionine",
    "GCG": "Alanine",
    "TCC": "Serine",
    "TAT": "Tyrosine",
    "CGT": "Arginine"
}

dna_sequence = "ATGCGTTATGCG"

proteins = []

for i in range(0, len(dna_sequence), 3):
    codon = dna_sequence[i:i+3]

    if len(codon) != 3:
        continue

    if codon in codon_table:
        proteins.append(codon_table[codon])

output = "-".join(proteins)

print("Sequence:", dna_sequence)
print("Proteins:", output)
