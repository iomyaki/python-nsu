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


with open('4.2_humanEnsembl.txt', 'r') as fin, open('4.2_humanEnsembl.orfs.txt', 'w') as fout:
    seq_name = fin.readline().rstrip()
    seq_itself = ''
    for line in fin:
        if '>' in line:
            for or_frame in range(3):
                if is_translatable(seq_itself, or_frame):
                    orf_out = f'+{or_frame}' if or_frame != 0 else '0'

                    fout.write(f'{seq_name}|{orf_out}\n')
                    fout.write(seq_itself)

            seq_name = line.rstrip()
            seq_itself = ''
        else:
            seq_itself += line
