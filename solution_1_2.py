# Jukes and Cantor model

def jukescantordist(seq1, seq2):
    from math import log

    if str(type(seq1)) != '<class \'str\'>' or str(type(seq2)) != '<class \'str\'>':
        return 'Input format is incorrect!'

    gencode = {'a', 'c', 'g', 't'}
    if set(seq1.lower()) != gencode or set(seq1.lower()) != gencode:
        return 'Input is not DNA sequences!'

    if len(seq1) != len(seq2):
        return 'Sequences are of different length!'

    mismatches = sum(1 for x, y in zip(seq1.lower(), seq2.lower()) if x != y)
    length = len(seq1)
    p = mismatches / length

    return f'{-3/4 * log(1 - 4/3 * p):.5f}'


print(jukescantordist('AtgcAtgcatgC', 'aTggatcgATgc'))
