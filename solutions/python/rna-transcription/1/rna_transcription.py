def to_rna(dna_strand):
    complement = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }

    rna = ""
    for nucleotide in dna_strand:
        rna += complement[nucleotide]

    return rna