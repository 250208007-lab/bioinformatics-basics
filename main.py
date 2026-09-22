print("=== Genetic Sequence Analysis Program ===")

dna_sequence = input("Enter a DNA sequence: ").upper()
total_bases = len(dna_sequence)


if total_bases > 0:
    g_Count = dna_sequence.count('G')
    c_Count = dna_sequence.count('C')
    
  
    gc_content = (g_Count + c_Count) / total_bases * 100
    
    rna_sequence = dna_sequence.replace('T', 'U')

    print("\n--- ANALYSIS RESULTS ---")
    print(f"Original DNA Sequence: {dna_sequence}")
    print(f"Transcribed RNA Sequence: {rna_sequence}")
    print(f"Total bases: {total_bases}")
    print(f"Guanine (G) count: {g_Count}")
    print(f"Cytosine (C) count: {c_Count}")
    print(f"GC Content: %{gc_content:.2f}")

    if "ATG" in dna_sequence:
        print("Start Codon (ATG): Found")
    else:
        print("Start Codon (ATG): Not Found")

else:
    print("Warning: You entered an empty sequence!")

