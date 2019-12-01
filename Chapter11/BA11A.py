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


def spectrum_graph(sp):
    sp.insert(0, 0)
    edges = []
    for i in range(len(sp)):
        for j in range(i, len(sp)):
            m1, m2 = sp[i], sp[j]
            if m2 - m1 in mass_to_aa:
                edges.append(str(m1) + '->' + str(m2) + ':' + mass_to_aa[m2-m1][0])
    return edges


def main():
    spectrum = list(map(int, sys.stdin.readline().split()))
    edges = spectrum_graph(spectrum)
    for edge in edges:
        print(edge)


if __name__ == '__main__':
    main()
