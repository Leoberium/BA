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
    163: ['Y'], 186: ['W']
}

# , 4: ['X'], 5: ['Z']


def peptide_sequencing(spectrum):
    m = len(spectrum)

    # constructing graph
    graph = [[] for _ in range(m + 1)]  # only in edges
    for v in range(m + 1):
        for mass in mass_to_aa:
            if v - mass >= 0:
                graph[v].append((v - mass, mass_to_aa[mass][0]))

    # maximum-weight path in a node-weighted DAG
    dist = [-10**6] * (m + 1)
    dist[0] = 0
    prev = [(-1, '')] * (m + 1)
    for v in range(1, m + 1):
        max_u, max_e = -1, ''
        for edge in graph[v]:
            u, e = edge
            d = dist[u] + spectrum[v-1]
            if d > dist[v]:
                dist[v] = d
                max_u, max_e = u, e
        prev[v] = (max_u, max_e)

    # backtracking
    v = m
    peptide = ''
    while v != 0:
        u, e = prev[v]
        peptide = e + peptide
        v = u

    return peptide


def main():
    spectrum = list(map(int, sys.stdin.readline().split()))
    print(peptide_sequencing(spectrum))


if __name__ == '__main__':
    main()
