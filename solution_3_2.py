def translation(seq, orf):
    """
    :param seq: nucleotide sequence of a coding strand, str
    :param orf: open reading frame start position, int
    :return: polypeptide if the sequence is translatable, error otherwise, str
    """

    genetic_code = {
        'UUU': 'F', 'UUC': 'F', 'UCU': 'S', 'UCC': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UGU': 'C', 'UGC': 'C',
        'UUA': 'L', 'UCA': 'S', 'UAA': None, 'UGA': None,
        'UUG': 'L', 'UCG': 'S', 'UAG': None, 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CCU': 'P', 'CCC': 'P',
        'CAU': 'H', 'CAC': 'H', 'CGU': 'R', 'CGC': 'R',
        'CUA': 'L', 'CUG': 'L', 'CCA': 'P', 'CCG': 'P',
        'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'ACU': 'T', 'ACC': 'T',
        'AAU': 'N', 'AAC': 'N', 'AGU': 'S', 'AGC': 'S',
        'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
        'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GCU': 'A', 'GCC': 'A',
        'GAU': 'D', 'GAC': 'D', 'GGU': 'G', 'GGC': 'G',
        'GUA': 'V', 'GUG': 'V', 'GCA': 'A', 'GCG': 'A',
        'GAA': 'E', 'GAG': 'E', 'GGA': 'G', 'GGG': 'G'}

    # transcribe
    complementarity = str.maketrans('ATGC', 'UACG')
    compl = seq.translate(complementarity)

    # find start codon
    start = compl.find('AUG')
    if start - orf < 0 or (start - orf) % 3 != 0:
        return 'Sequence not translatable: No start codon'

    # check if the stop codon immediately follows the start codon
    if compl.find('UAA') == start + 3 or compl.find('UGA') == start + 3 or compl.find('UAG') == start + 3:
        return 'Sequence not translatable: No codons between start and stop'

    # translate
    polypeptide = ''
    for i in range(start, len(compl) - 2, 3):
        triplet = compl[i] + compl[i + 1] + compl[i + 2]
        if genetic_code[triplet] is not None:
            polypeptide += genetic_code[triplet]
        else:
            break

    return polypeptide


print(translation('GGTGTGGATTGTAGAGCCTACCTTACTCTTCCGGGGAATACTAAGCATAGTTATTAGCGTAGCGAGTACGAGTTTCCACGTCGGAGGTGTCGCTGATGAC', 0))
