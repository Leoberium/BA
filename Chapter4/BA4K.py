import sys


aa_int_masses = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97,
    'V': 99, 'T': 101, 'C': 103, 'I': 113,
    'L': 113, 'N': 114, 'D': 115, 'K': 128,
    'Q': 128, 'E': 129, 'M': 131, 'H': 137,
    'F': 147, 'R': 156, 'Y': 163, 'W': 186
}


def mass(peptide):
    m = 0
    if not peptide:
        return m
    for aa in peptide:
        m += aa_int_masses[aa]
    return m


def linear_spectrum(peptide):
    s = [0]
    n = len(peptide)
    for k in range(1, n + 1):
        for i in range(n - k + 1):
            sub_peptide = peptide[i:i+k]
            s.append(mass(sub_peptide))
    return s


def linear_score(peptide, spectrum):
    if not peptide:
        return 0
    peptide_spectrum = linear_spectrum(peptide)
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
    print(linear_score(peptide, spectrum))


if __name__ == '__main__':
    main()
