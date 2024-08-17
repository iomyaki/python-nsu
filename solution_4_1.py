def create_seq(file):
    from random import sample

    header = file.readline().rstrip().split('\t')
    for line in file:
        try:
            splitted_line = line.split('\t')
            n_0, n_1, n_2, n_3 = map(int, splitted_line)
            nucleotides = header[0] * n_0 + header[1] * n_1 + header[2] * n_2 + header[3] * n_3
            yield ''.join(sample(nucleotides, len(nucleotides)))
        except ValueError:
            yield 'Incorrect input'


with open('4.1_exception.txt') as txt_file:
    print(*tuple(create_seq(txt_file)), sep='\n')
