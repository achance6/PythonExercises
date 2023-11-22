def to_rna(dna_strand: str) -> str:
    # cool (and fast) way
    LOOKUP = str.maketrans('ACGT', 'UGCA')

    return dna_strand.translate(LOOKUP)

    # First try
    # dna_to_rna = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    # rna_strand = ''
    # for nucleotide in dna_strand:
    #     rna_strand += dna_to_rna[nucleotide]
    # return rna_strand