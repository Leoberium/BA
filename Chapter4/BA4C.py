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


def main():
    peptide = input()
    print(*cyclospectrum(peptide))


if __name__ == '__main__':
    main()
