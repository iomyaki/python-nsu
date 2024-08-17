import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import log


def create_naïve_consensus(MSA):
    bases = ('A', 'T', 'G', 'C')

    num_seqs = len(MSA)
    seq_len = len(MSA[0])
    alignment = list(zip(*MSA))

    output = ''
    for pos in range(seq_len):
        pos_nucleotides = ''.join(list(alignment[pos]))
        frequencies = {base: pos_nucleotides.count(base) / num_seqs for base in bases}

        commonest_nucleotide = max(zip(frequencies.values(), frequencies.keys()))[1]
        output += commonest_nucleotide

    return output


def seqs_unlikeness(seq1, seq2):
    mismatches = sum(1 for nuc_1, nuc_2 in zip(seq1, seq2) if nuc_1 != nuc_2)
    length = len(seq1)
    p = mismatches / length

    return p


df = pd.read_excel('sequences_7.1.xlsx')
taxa = pd.read_csv('taxas_7.1.csv')

# create consensus
sequences = []
for _, row in df.iterrows():
    sequences.append(row[1])

consensus = create_naïve_consensus(sequences)
L = len(consensus)

# find differences between the consensus and sequences
differences = []
for _, row in df.iterrows():
    differences.append(seqs_unlikeness(row[1], consensus))

df['p-dist'] = differences

# find Jukes–Cantor distances
jukes_cantor_dists = []
for _, row in df.iterrows():
    try:
        jukes_cantor_dists.append(-3 / 4 * log(1 - 4 / 3 * row[2]))
    except ValueError:
        jukes_cantor_dists.append('NaN')

df['JC'] = jukes_cantor_dists

# find Kimura distances
kimura_dists = []
for _, row in df.iterrows():
    try:
        transitions = (('A', 'G'), ('G', 'A'), ('T', 'C'), ('C', 'T'))
        transversions = (('A', 'T'), ('A', 'C'), ('G', 'C'), ('G', 'T'), ('T', 'A'), ('T', 'G'), ('C', 'A'), ('C', 'G'))
        P = sum(1 for nuc_1, nuc_2 in zip(row[1], consensus) if (nuc_1, nuc_2) in transitions) / L
        Q = sum(1 for nuc_1, nuc_2 in zip(row[1], consensus) if (nuc_1, nuc_2) in transversions) / L
        kimura_dists.append(-1 / 2 * log(1 - 2 * P - Q) - 1 / 4 * log(1 - 2 * Q))
    except ValueError:
        kimura_dists.append('NaN')

df['K2P'] = kimura_dists

# violin plot
df['non-full'] = df.eq('NaN').any(axis=1).astype(int)

fullnesses = []
for _, row in df.iterrows():
    fullnesses.append('all 3 distances' if row[5] == 0 else 'not all 3 distances')

df['fullness'] = fullnesses

sns.violinplot(x=df['fullness'], y=df['p-dist'])
plt.show()

df = df.drop(['non-full', 'fullness'], axis=1)

# merge with another table
merged_df = pd.merge(df, taxa, on='number')
cleansed_df = merged_df.drop(merged_df[(merged_df['cell_type'] == 'unknown')].index)

# taxa bar plot
taxa_count = cleansed_df.groupby(['taxa_name'])['taxa_name'].count()

taxa_count.plot.bar(rot=0)
plt.show()

# save as *.tsv
cleansed_df.to_csv('merged_7.1.tsv', sep='\t')
