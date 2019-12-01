import sys


aa_to_mass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
    'T': 101, 'C': 103, 'L': 113, 'I': 113, 'N': 114,
    'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186,
    'X': 4, 'Z': 5
}

mass_to_aa = {
    57: ['G'], 71: ['A'], 87: ['S'], 97: ['P'],
    99: ['V'], 101: ['T'], 103: ['C'], 113: ['L', 'I'],
    114: ['N'], 115: ['D'], 128: ['K', 'Q'], 129: ['E'],
    131: ['M'], 137: ['H'], 147: ['F'], 156: ['R'],
    163: ['Y'], 186: ['W'], 4: ['X'], 5: ['Z']
}


def peptide_to_mass(peptide):
    m = 0
    for aa in peptide:
        m += aa_to_mass[aa]
    return m


def score(peptide, spectrum):
    p = list(peptide)[::-1]
    s = 0
    i = -1
    while p:
        aa = p.pop()
        i += aa_to_mass[aa]
        s += spectrum[i]
    return s


def peptide_identification(spectrum, proteome):
    m = len(spectrum)  # target mass
    n = len(proteome)

    # trying all peptides
    max_score, max_peptide = -10**6, ''
    for length in range(4, 20):
        for i in range(n - length + 1):
            peptide = proteome[i:i+length]
            mass = peptide_to_mass(peptide)
            if mass != m:
                continue
            else:
                s = score(peptide, spectrum)
                if s > max_score:
                    max_score = s
                    max_peptide = peptide

    return max_peptide, max_score


def psm_search(sv, proteome, threshold):
    psm_set = []
    for spectrum in sv:
        peptide, p_score = peptide_identification(spectrum, proteome)
        if p_score >= threshold:
            psm_set.append(peptide)
    return psm_set


def main():
    lines = []
    for line in sys.stdin:
        line = line.strip()
        lines.append(line)
    threshold = int(lines.pop())
    proteome = lines.pop()
    spectral_vectors = []
    for line in lines:
        spectrum = list(map(int, line.split()))
        spectral_vectors.append(spectrum)
    for peptide in psm_search(spectral_vectors, proteome, threshold):
        print(peptide)


if __name__ == '__main__':
    main()
