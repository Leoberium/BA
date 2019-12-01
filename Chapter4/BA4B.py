import sys


dna_to_protein = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '0', 'TAG': '0',
    'TGT': 'C', 'TGC': 'C', 'TGA': '0', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}


aa_to_dna = {'F': ['TTT', 'TTC'],
             'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
             'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
             'Y': ['TAT', 'TAC'],
             'C': ['TGT', 'TGC'],
             'W': ['TGG'],
             'P': ['CCT', 'CCC', 'CCA', 'CCG'],
             'H': ['CAT', 'CAC'],
             'Q': ['CAA', 'CAG'],
             'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
             'I': ['ATT', 'ATC', 'ATA'],
             'M': ['ATG'],
             'T': ['ACT', 'ACC', 'ACA', 'ACG'],
             'N': ['AAT', 'AAC'],
             'K': ['AAA', 'AAG'],
             'V': ['GTT', 'GTC', 'GTA', 'GTG'],
             'A': ['GCT', 'GCC', 'GCA', 'GCG'],
             'D': ['GAT', 'GAC'],
             'E': ['GAA', 'GAG'],
             'G': ['GGT', 'GGC', 'GGA', 'GGG']
}


def rev_comp(s):
    c = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    rs = ''
    for ch in s:
        rs += c[ch]
    return rs[::-1]


def generate_dna(peptide):
    if len(peptide) == 1:
        for codon in aa_to_dna[peptide]:
            yield codon
    else:
        prefix = peptide[:-1]
        suffix = peptide[-1]
        for codon in aa_to_dna[suffix]:
            for p in generate_dna(prefix):
                yield p + codon


def encoding_substrings(dna, peptide):
    substrings = []
    n = len(dna)
    k = len(peptide) * 3
    encoding = []
    for s in generate_dna(peptide):
        rs = rev_comp(s)
        encoding.append(s)
        encoding.append(rs)
    for i in range(n - k + 1):
        substring = dna[i:i+k]
        if substring in encoding:
            substrings.append(substring)
    return substrings


def main():
    text = sys.stdin.readline().strip()
    peptide = sys.stdin.readline().strip()
    substrings = encoding_substrings(text, peptide)
    for substring in substrings:
        print(substring)


if __name__ == '__main__':
    main()
