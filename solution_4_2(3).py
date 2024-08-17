def find_start(seq, orf):
    start = -1
    for i in range(orf, len(seq) - 2, 3):
        if seq[i:i + 3] == 'ATG':
            start = i
            break

    return start


def is_translatable(seq, orf):
    start = find_start(seq, orf)

    if start == -1:
        return False

    try:
        if seq[start + 3:start + 6] in ('TAA', 'TGA', 'TAG'):
            return False
    except IndexError:
        return True

    return True


def translate(seq, orf):
    genetic_code = {'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
                    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
                    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
                    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
                    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
                    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
                    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
                    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
                    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
                    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
                    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
                    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
                    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
                    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
                    'TAC': 'Y', 'TAT': 'Y', 'TAA': None, 'TAG': None,
                    'TGC': 'C', 'TGT': 'C', 'TGA': None, 'TGG': 'W'
                    }

    start = find_start(seq, orf)

    polypeptide = ''
    for i in range(start, len(seq) - 2, 3):
        triplet = seq[i] + seq[i + 1] + seq[i + 2]
        if genetic_code[triplet] is not None:
            polypeptide += genetic_code[triplet]
        else:
            break

    return polypeptide


with open('4.2_humanEnsembl.txt', 'r') as fin, open('4.2_humanEnsembl.translation.txt', 'w') as fout:
    seq_name = fin.readline().rstrip().split('|')[0]
    seq_itself = ''
    for line in fin:
        if '>' in line:
            for or_frame in range(3):
                if is_translatable(seq_itself, or_frame):
                    fout.write(f'{seq_name}_{or_frame}\n')
                    protein = translate(seq_itself, or_frame)
                    fout.write(f'{protein}\n\n')

            seq_name = line.split('|')[0]
            seq_itself = ''
        else:
            seq_itself += line.rstrip()
