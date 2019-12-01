import sys

masses = [
    57, 71, 87, 97, 99,
    101, 103, 113, 114, 115,
    128, 129, 131, 137, 147,
    156, 163, 186
]


def expand(ps):
    for peptide in ps.copy():
        ps.remove(peptide)
        for m in masses:
            if peptide:
                new_peptide = peptide + '-' + str(m)
            else:
                new_peptide = str(m)
            ps.add(new_peptide)
    return ps


def mass(peptide):
    m = sum(map(int, peptide.split('-')))
    return m


def cyclospectrum(peptide):
    cs = [0]
    composition = list(map(int, peptide.split('-')))
    n = len(composition)
    for k in range(1, n):
        for i in range(n):
            if i + k <= n:
                cs.append(sum(composition[i:i+k]))
            else:
                r = i + k - n
                cs.append(sum(composition[i:] + composition[:r]))
    cs.append(mass(peptide))
    cs.sort()
    return cs


def linear_spectrum(peptide):
    cs = [0]
    composition = list(map(int, peptide.split('-')))
    n = len(composition)
    for k in range(1, n):
        for i in range(n - k + 1):
            cs.append(sum(composition[i:i+k]))
    cs.append(mass(peptide))
    cs.sort()
    return cs


def not_consistent(peptide, spectrum):
    peptide_spectrum = linear_spectrum(peptide)
    for value in peptide_spectrum:
        if value not in spectrum:
            return True
    return False


def cyclopeptide_sequencing(spectrum):
    peptides = {''}
    matches = set()
    parent_mass = max(spectrum)
    while peptides:
        peptides = expand(peptides)
        for peptide in peptides.copy():
            if mass(peptide) == parent_mass:
                if cyclospectrum(peptide) == spectrum:
                    matches.add(peptide)
                peptides.remove(peptide)
            elif not_consistent(peptide, spectrum):
                peptides.remove(peptide)
    return matches


def main():
    spectrum = list(map(int, sys.stdin.readline().split()))
    print(*cyclopeptide_sequencing(spectrum))


if __name__ == '__main__':
    main()
