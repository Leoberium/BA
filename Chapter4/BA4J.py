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
    prefix_mass = [0]
    n = len(peptide)
    for i in range(n):
        prefix_mass.append(prefix_mass[-1] + mass(peptide[i]))
    for i in range(n):
        for j in range(i + 1, n + 1):
            s.append(prefix_mass[j] - prefix_mass[i])
    s.sort()
    return s


def main():
    peptide = sys.stdin.readline().strip()
    print(*linear_spectrum(peptide))


if __name__ == '__main__':
    main()
