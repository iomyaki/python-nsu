from random import choice


# Subtask #1
def position_frequencies(MSA):
    """
    :param MSA: multiple sequence alignment, list
    :return: nucleotide frequencies on each position of an alignment, str
    """

    num_seqs = len(MSA)
    seq_len = len(MSA[0])
    alignment = list(zip(*MSA))

    output = ''
    for pos in range(seq_len):
        pos_nucleotides = ''.join(list(alignment[pos]))
        freq_a = pos_nucleotides.count('A') / num_seqs
        freq_t = pos_nucleotides.count('T') / num_seqs
        freq_g = pos_nucleotides.count('G') / num_seqs
        freq_c = pos_nucleotides.count('C') / num_seqs

        output += f'Pos. {pos + 1}: A: {freq_a:.3f}; T: {freq_t:.3f}; G: {freq_g:.3f}; C: {freq_c:.3f}\n'

    return output


# Subtask #2
def sequences_stats(MSA):
    """
    :param MSA: multiple sequence alignment, list
    :return: nucleotide composition of each sequence in an alignment, str
    """

    output = ''
    for i in range(len(MSA)):
        stats = {'A': MSA[i].count('A'),
                 'T': MSA[i].count('T'),
                 'G': MSA[i].count('G'),
                 'C': MSA[i].count('C')
                 }
        output += (f'Seq. {i + 1}: A: ' + str(stats['A'])
                   + '; T: ' + str(stats['T'])
                   + '; G: ' + str(stats['G'])
                   + '; C: ' + str(stats['C']) + '\n'
                   )

    return output


# Subtask #3
def create_consensus(MSA):
    """
    :param MSA: multiple sequence alignment, list
    :return: consensus sequence of an alignment, str
    """

    num_seqs = len(MSA)
    seq_len = len(MSA[0])
    alignment = list(zip(*MSA))

    degenerate_nucleotides = {(0,): 'A', (1,): 'T', (2,): 'G', (3,): 'C', (0, 1): 'W', (0, 2): 'R', (0, 3): 'M',
                              (1, 2): 'K', (1, 3): 'Y', (2, 3): 'S', (0, 1, 2): 'D', (0, 1, 3): 'H', (1, 2, 3): 'B',
                              (0, 2, 3): 'V', (0, 1, 2, 3): 'N'}

    output = ''
    for pos in range(seq_len):
        pos_nucleotides = ''.join(list(alignment[pos]))
        # in the "frequencies" list, nucleotides follow the order: A, T, G, C, so index 0 corresponds to A, 1 to T etc.
        frequencies = [pos_nucleotides.count('A') / num_seqs,
                 pos_nucleotides.count('T') / num_seqs,
                 pos_nucleotides.count('G') / num_seqs,
                 pos_nucleotides.count('C') / num_seqs
                 ]

        max_freq = max(frequencies)
        indices = []
        for index in range(4):
            if frequencies[index] == max_freq:
                indices.append(index)

        output += degenerate_nucleotides[tuple(indices)]

    return output


sequences = [''.join(choice(('A', 'T', 'G', 'C')) for _ in range(10)) for _ in range(6)]

print(*sequences, end='\n\n')
print(position_frequencies(sequences))
print(sequences_stats(sequences))
print(create_consensus(sequences))
