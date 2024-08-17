import matplotlib.pyplot as plt


def create_consensus(MSA):
    num_seqs = len(MSA)
    seq_len = len(MSA[0])
    alignment = list(zip(*MSA))

    degenerate_nucleotides = {
        (0,): 'A', (1,): 'T', (2,): 'G', (3,): 'C', (0, 1): 'W', (0, 2): 'R', (0, 3): 'M', (1, 2): 'K', (1, 3): 'Y',
        (2, 3): 'S', (0, 1, 2): 'D', (0, 1, 3): 'H', (1, 2, 3): 'B', (0, 2, 3): 'V', (0, 1, 2, 3): 'N'
    }

    output = ''
    for pos in range(seq_len):
        pos_nucleotides = ''.join(list(alignment[pos]))
        # in the "frequencies" list, nucleotides follow the order: A, T, G, C, so index 0 corresponds to A, 1 to T etc.
        frequencies = (
            pos_nucleotides.count('A') / num_seqs,
            pos_nucleotides.count('T') / num_seqs,
            pos_nucleotides.count('G') / num_seqs,
            pos_nucleotides.count('C') / num_seqs
        )

        max_freq = max(frequencies)
        indices = []
        for index in range(4):
            if frequencies[index] == max_freq:
                indices.append(index)

        output += degenerate_nucleotides[tuple(indices)]

    return output


with open('5.1_MSA.txt') as fin:
    MSA = []
    for line in fin:
        MSA.append(line.rstrip())

consensus = create_consensus(MSA)
nucleotides = {i: consensus.count(i) for i in set(consensus)}

plt.pie(nucleotides.values(), labels=nucleotides.keys())

plt.axis('equal')
plt.show()
