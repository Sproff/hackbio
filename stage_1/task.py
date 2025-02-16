# import matplotlib.pyplot as plt
# import numpy as np

# Task 1
DNA_SEQUENCE = "ATGGCTTACGGA"

# Genetic Code Dictionary
genetic_code = {
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "UAU": "Y",
    "UAC": "Y",
    "UAA": "Stop",
    "UAG": "Stop",
    "UGU": "C",
    "UGC": "C",
    "UGA": "Stop",
    "UGG": "W",
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",  # Start codon (Methionine)
    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}


# Convert DNA to mRNA
def convert_dna_to_mrna(dna: str):
    return dna.upper().replace("T", "U")


# Convert mRNA to Protein
def convert_mrna_to_protein(mrna: str):
    protein_sequence = []

    # Split mRNA into codons (3 nucleotides each)
    for i in range(0, len(mrna), 3):
        codon = mrna[i : i + 3]

        # Stop translation if codon is shorter than 3 bases (incomplete codon)
        if len(codon) < 3:
            break

        # Look up codon in genetic code dictionary
        amino_acid = genetic_code.get(codon, "?")  # "?" for unknown codons

        if amino_acid == "Stop":
            break

        protein_sequence.append(amino_acid)

    return "".join(protein_sequence)


# Test the functions
mRNA_SEQUENCE = convert_dna_to_mrna(DNA_SEQUENCE)
protein = convert_mrna_to_protein(mRNA_SEQUENCE)


# Task 2
"""
f(x)= \frac {L}{1+ e^{-k(x-x_0)}}
f(x)	=	output of the function
L	=	the curve's maximum value
k	=	logistic growth rate or steepness of the curve
x_0	=	the x value of the sigmoid midpoint
x	=	real number
"""
# Constant e value
e = 2.718281828459045


def logistic(L: float, k: float, x0: float, x: int):
    f = L / (1 + pow(e, -k * (x - x0)))
    return f


variables = list(range(-5, 100))

L = 10
k = 1.5  # the higher the k, the steeper the curve will be, and the lower the k, the flatter the curve
x0 = 2


logistic_vals = []

for x in variables:
    y = logistic(L=L, k=k, x0=x0, x=x)
    logistic_vals.append(y)

# Plotting of graph
# plt.plot(variables, logistic_vals)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Logistic Function")
# plt.savefig("graph.png")


# Task 3
def time_to_80_percent(k, x0):
    """
    Determines the time (x) to reach 80% of the maximum growth (carrying capacity).
    Parameters:
        k (float): Growth rate
        x0 (float): Midpoint of the logistic curve
    Returns:
        float: Time to reach 80% of L
    """
    return x0 - (-0.60205999 / k)


# Task 4
def hamming_distance(str1: str, str2: str) -> int:
    max_length = max(len(str1), len(str2))

    # Pad the shorter string with spaces
    str1 = str1.ljust(max_length)
    str2 = str2.ljust(max_length)

    return sum(1 for a, b in zip(str1, str2) if a != b)


distance = hamming_distance("Sproff", "dev_sproff")
