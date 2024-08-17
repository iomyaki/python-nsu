import matplotlib.pyplot as plt
import seaborn as sns


def add_commonest_nucleotide(lst):
    global consensus

    nucleotides = {'A': lst[1], 'T': lst[2], 'G': lst[3], 'C': lst[4]}
    commonest_nucleotide = max(zip(nucleotides.values(), nucleotides.keys()))[1]

    consensus += commonest_nucleotide


with open('6_coverage.txt') as dt, open('6_reference_seq.fasta') as ref:
    data = []
    dt.readline()  # skip the first line
    for line in dt:
        splitted_line = line.split('\t')[1:]
        data.append(tuple(map(int, splitted_line)))

    reference = ''
    ref.readline()  # skip the first line
    for line in ref:
        reference += line.rstrip()

coverage_threshold = 80
ref_length = len(reference)

consensus = ''
latest = 0
for row in data:
    if row[0] == latest + 1:
        if row[5] < coverage_threshold:
            consensus += '-'
        else:
            add_commonest_nucleotide(row)

    else:
        consensus += '-' * (row[0] - (latest + 1))
        add_commonest_nucleotide(row)

    latest = row[0]

consensus += '-' * (ref_length - latest)  # in case the end of the reference is not covered

# ======
# Part 1
# ======

len_wo_dashes = len(consensus.replace('-', ''))
stats = {'A': consensus.count('A'),
         'T': consensus.count('T'),
         'G': consensus.count('G'),
         'C': consensus.count('C')
         }

gc_content = (stats['G'] + stats['C']) / len_wo_dashes

print(f'GC-content: {gc_content}')

# ======
# Part 2
# ======

x = list(stats.keys())
y = list(stats.values())
colors = ['Green', 'Red', 'Black', 'Blue']

fig = plt.figure(figsize=(8, 5))
plt.bar(x, y, color=colors, width=0.5)

for i in range(len(x)):
    plt.text(i, y[i] / 2, y[i], ha='center', color='White')

plt.xlabel('Nucleotide')
plt.ylabel('Amount')
plt.title('Nucleotide composition of a consensus')
plt.show()

# ======
# Part 3
# ======

coverage = list(tuple(zip(*data))[5])
num_covered_positions = len(data)
coverage.extend([0] * (ref_length - num_covered_positions))

#fig1 = plt.figure(figsize=(8, 5))
#sns.kdeplot(coverage, color='b', fill=True)
#plt.xlabel('Coverage')
#plt.ylabel('Probability density')
#plt.title('KDE of genome coverage')
#plt.show()

fig2 = plt.figure(figsize=(8, 5), dpi=100)
sns.histplot(coverage, bins=30, color='b', kde=True)
plt.xlabel('Coverage')
plt.title('KDE + histogram')
plt.show()
