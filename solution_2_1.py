sequence = 'ATGCCGTACACAGTGAGAGACATATG'
MGE = 'GAGAGACA'
position = sequence.index(MGE)

print(f'MGE is on position {position}' if position != -1 else 'There is no mob')
print(sequence.replace('GAGAGACA', 'gagagaca'))
