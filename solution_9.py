import re
import requests
import numpy as np


def parsing_gene(taxa, gene_number):
    url = f'https://www.kegg.jp/entry/{taxa}:{gene_number}'
    resp = requests.get(url=url)

    lines = resp.text.splitlines()  # "lines" is a list

    read_network, read_position, read_aa, read_nt = False, False, False, False
    aa_sequence, nt_sequence = '', ''
    for line in lines:
        if not line:
            read_aa, read_nt = False, False
        elif read_nt:
            nt_sequence += re.sub('<(.*?)>', '', line.rstrip())
        elif read_aa:
            aa_sequence += re.sub('<(.*?)>', '', line.rstrip())
        elif read_position:
            position = line
            read_position = False
        elif read_network:
            phenotypes = line
            read_network = False
        elif 'Position' in line:
            read_position = True
        elif 'Network' in line:
            read_network = True
        elif 'NT seq' in line and 'nt' in line:
            read_nt = True
        elif 'AA seq' in line and 'aa' in line:
            read_aa = True
        else:
            continue

    # NETWORK
    try:
        # remove contents of angle brackets, then remove "&nbsp;"
        phenotypes = re.sub('<(.*?)>', '<>', phenotypes).replace('&nbsp;', '')

        # split by angle brackets, creating a list
        phenotypes_list = phenotypes.split('<>')

        # remove empty elements from the list
        phenotypes_list = list(filter(None, phenotypes_list))

        # make dictionary with phenotypes
        phenotypes_dict = dict(zip(phenotypes_list[::2], phenotypes_list[1::2]))

    except UnboundLocalError:  # because will not work with some species, e.g. Mus musculus
        phenotypes_dict = 'No phenotypes found'

    # POSITION
    # remove angle brackets and what is inside them
    position = re.sub('<(.*?)>', '', position)

    # reformat coordinates according to the task
    position = 'chr' + position.replace('..', '-')

    return phenotypes_dict, nt_sequence, aa_sequence, position


def parsing_ortho(taxa, gene_number):
    url = f'https://www.kegg.jp/ssdb-bin/ssdb_best?org_gene={taxa}:{gene_number}'
    resp = requests.get(url=url)

    lines = resp.text.splitlines()

    num_entries = [10, 100, 200, 500]

    list_sw_scores, list_identities = [], []
    gene_counter = 0
    for line in lines:
        if 'INPUT TYPE="checkbox"' in line:
            gene_info = re.sub('<(.*?)>', '', line)
            gene_info_list = gene_info.split()
            i = gene_info_list.index('(')  # index of the left parenthesis
            list_sw_scores.append(int(gene_info_list[i - 1]))
            list_identities.append(float(gene_info_list[i + 3]))

            gene_counter += 1
            if gene_counter == 500:
                break

    if gene_counter < max(num_entries):
        num_entries = [num for num in num_entries if num < gene_counter]
        num_entries.append(gene_counter)

    for num in num_entries:
        pearson = np.corrcoef(list_sw_scores[:num], list_identities[:num])
        yield f'{num} orthologs - {pearson[0][1]}'


species = 'hsa'
gene = '7314'

print('PARSING_GENE:')
for entry in parsing_gene(species, gene):
    print(entry)
print()
print('PARSING_ORTHO:')
for entry in parsing_ortho(species, gene):
    print(entry)
