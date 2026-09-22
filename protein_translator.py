print("---Protein Translator and Amino Acid Counter---")
rna_sequence = input("Please enter a Rna kodon sequence with three letters (e.g. AUG): ").upper()
if rna_sequence == "":
    print("RNA sequence cannot be empty.")
elif len(rna_sequence) != 3:
    print("RNA sequence must be exactly 3 letters long.")
elif rna_sequence == "AUG":
    print("The amino acid is Methionine (Start codon).")
elif rna_sequence == "GCU" or rna_sequence == "GCC":
    print("The amino acid is Alanine.")
elif rna_sequence == "UAA" or rna_sequence == "UGA":
    print("The amino acid is a Stop codon.")
else:
    print("The amino acid is not recognized.")
