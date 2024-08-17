import matplotlib.pyplot as plt


def add_commonest_nucleotide(lst):
    global consensus

    nucleotides = {'A': lst[1], 'T': lst[2], 'G': lst[3], 'C': lst[4]}
    commonest_nucleotide = max(zip(nucleotides.values(), nucleotides.keys()))[1]

    consensus += commonest_nucleotide


def nucleotide_contents(step, window, length, mode='AT'):
    def get_upper_limit(step, window, length):
        n = 0
        while step * n + window <= length - window:
            n += 1

        return step * (n - 1) + window

    global consensus

    upper_limit = get_upper_limit(step, window, length)

    contents = []
    for i in range(0, upper_limit, step):
        section = consensus[i:i + window]
        content_section = (section.count(mode[0]) + section.count(mode[1])) / window
        contents.append(content_section)

    return contents


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
            consensus += reference[latest]
        else:
            add_commonest_nucleotide(row)

    else:
        consensus += reference[latest:row[0] - 1]
        add_commonest_nucleotide(row)

    latest = row[0]

consensus += reference[latest:]  # in case the end of the reference is not covered

# ======
# Part 1
# ======

length = len(consensus)
stats = {'A': consensus.count('A'),
         'T': consensus.count('T'),
         'G': consensus.count('G'),
         'C': consensus.count('C')
         }

gc_content = (stats['G'] + stats['C']) / length

print(f'GC-content: {gc_content}')

# ======
# Part 2
# ======

window = length // 100
step = length // 1000

at_contents = nucleotide_contents(step, window, length)
gc_contents = [1 - at for at in at_contents]

fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(8, 6))
fig.suptitle('Sliding window')

ax1.plot(at_contents, 'tab:red')
ax2.plot(gc_contents, 'tab:green')

ax1.set_title('AT-content')
ax2.set_title('GC-content')

plt.show()
