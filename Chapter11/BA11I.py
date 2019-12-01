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
    163: ['Y'], 186: ['W']  # , 4: ['X'], 5: ['Z']
}


def probability_of_spectral_dictionary(spectrum, threshold, max_score):
    m = len(spectrum)

    # computing masses to account for repeated masses
    masses = []
    for mass in mass_to_aa:
        masses += [mass] * len(mass_to_aa[mass])

    table = [[.0] * (m + 1) for _ in range(max_score + 1)]

    # initializing empty peptide
    table[0][0] = 1.0
    spectrum.insert(0, 0)

    # filling the table
    for i in range(1, m + 1):
        for t in range(max_score + 1):

            d = t - spectrum[i]
            if d < 0 or d > max_score:
                continue

            s = 0
            for mass in masses:
                if i - mass < 0:
                    continue
                s += table[d][i - mass]

            table[t][i] = s / 20

    return sum((table[t][-1] for t in range(threshold, max_score + 1)))


def main():
    spectrum = list(map(int, sys.stdin.readline().split()))
    threshold = int(sys.stdin.readline())
    max_score = int(sys.stdin.readline())
    print(probability_of_spectral_dictionary(spectrum, threshold, max_score))


if __name__ == '__main__':
    main()
