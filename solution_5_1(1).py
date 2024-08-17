import numpy as np
import matplotlib.pyplot as plt


def position_frequencies(MSA):
    num_seqs = len(MSA)
    seq_len = len(MSA[0])
    alignment = list(zip(*MSA))

    frequencies = []

    for pos in range(seq_len):
        pos_nucleotides = ''.join(list(alignment[pos]))
        freq_a = pos_nucleotides.count('A') / num_seqs
        freq_t = pos_nucleotides.count('T') / num_seqs
        freq_g = pos_nucleotides.count('G') / num_seqs
        freq_c = pos_nucleotides.count('C') / num_seqs

        pos_freqs = [freq_a, freq_t, freq_g, freq_c]
        frequencies.append(pos_freqs)

    return frequencies


def vector_addition(vec1, vec2):
    return [vec1[j] + vec2[j] for j in range(len(vec1))]


with open('5.1_MSA.txt') as fin:
    MSA = []
    for line in fin:
        MSA.append(line.rstrip())

freqs = position_frequencies(MSA)

# define chart parameters
freqs_graph = tuple(map(tuple, zip(*freqs)))
xloc = [i for i in range(len(MSA[0]))]

# create stacked bar chart
A = plt.bar(xloc, freqs_graph[0])
bottom = freqs_graph[0]

T = plt.bar(xloc, freqs_graph[1], bottom=bottom)
bottom = vector_addition(bottom, freqs_graph[1])

G = plt.bar(xloc, freqs_graph[2], bottom=bottom)
bottom = vector_addition(bottom, freqs_graph[2])

C = plt.bar(xloc, freqs_graph[3], bottom=bottom)

# add title, labels, tick marks, and legend
plt.title('MSA')
plt.xlabel('Alignment position')
plt.ylabel('Frequency')
plt.xticks(xloc, ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII'))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.legend((A[0], T[0], G[0], C[0]), ('A', 'T', 'G', 'C'))

# display chart
plt.show()
