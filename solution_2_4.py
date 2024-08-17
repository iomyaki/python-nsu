aa_dict = {'Trp': 5, 'Asn': 3,
           'Lys': 1, 'Leu': 2,
           'Ile': 9, 'Val': 10,
           'Ser': 1, 'Tyr': 2}

if aa_dict['Trp'] > aa_dict['Tyr']:
    aa_dict['Lys'] += 2

if aa_dict['Val'] < (aa_dict['Ile'] + aa_dict['Leu']):
    del aa_dict['Val']

if aa_dict['Ser'] == 1:
    aa_dict['Gly'] = sum(aa_dict.values())  # !

aa_dict['Arg'] = aa_dict.pop('Lys')  # !

print(aa_dict)
