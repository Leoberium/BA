import sys


aa_int_masses = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97,
    'V': 99, 'T': 101, 'C': 103, 'I': 113,
    'L': 113, 'N': 114, 'D': 115, 'K': 128,
    'Q': 128, 'E': 129, 'M': 131, 'H': 137,
    'F': 147, 'R': 156, 'Y': 163, 'W': 186
}


def cyclic_peptides(peptide):
    n = len(peptide)
    sub_peptides = ['']
    for k in range(1, n):
        for i in range(n):
            if i + k <= n:
                sub_peptides.append(peptide[i:i+k])
            else:
                residual = i + k - n
                sub_peptides.append(peptide[i:] + peptide[:residual])
    sub_peptides.append(peptide)
    return sub_peptides


def cyclospectrum(peptide):
    sp = cyclic_peptides(peptide)
    spectrum = []
    for s in sp:
        mass = 0
        for ch in s:
            mass += aa_int_masses[ch]
        spectrum.append(mass)
    spectrum.sort()
    return spectrum


def score(peptide, spectrum):
    peptide_spectrum = cyclospectrum(peptide)
    p_dict, s_dict = dict(), dict()
    for value in peptide_spectrum:
        if value in p_dict:
            p_dict[value] += 1
        else:
            p_dict[value] = 1
    for value in spectrum:
        if value in s_dict:
            s_dict[value] += 1
        else:
            s_dict[value] = 1
    s = 0
    for value in p_dict:
        if value in s_dict:
            s += min(p_dict[value], s_dict[value])
    return s


def main():
    peptide = sys.stdin.readline().strip()
    spectrum = list(map(int, sys.stdin.readline().split()))
    print(score(peptide, spectrum))


if __name__ == '__main__':
    main()
