sequence = 'ACCTGATGATAACTA'
seqList = list(sequence)
stop = ['T', 'G', 'A']

newSeqList = seqList[:-3] + stop

newSeqList.insert(0, 'G')
newSeqList.insert(0, 'T')
newSeqList.insert(0, 'A')

print(''.join(newSeqList))
print(len(newSeqList))
