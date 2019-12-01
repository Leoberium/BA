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


def ideal_spectrum(peptide):
    sp = []

    for i in range(len(peptide)):
        prefix, suffix = peptide[:i], peptide[i:]
        sp.append(peptide_to_mass(prefix))
        sp.append(peptide_to_mass(suffix))

    sp.sort()

    return sp


def graph_construction(spectrum):
    n = len(spectrum)
    graph = {}

    for i in range(n):
        for j in range(i + 1, n):
            d = spectrum[j] - spectrum[i]
            if d not in mass_to_aa:
                continue
            u, v = spectrum[i], spectrum[j]
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            for aa in mass_to_aa[d]:
                graph[u].append((v, aa))

    return graph


def reverse_graph(g):
    gr = {}
    for u in g:
        for edge in g[u]:
            v, aa = edge
            if v not in gr:
                gr[v] = []
            if u not in gr:
                gr[u] = []
            gr[v].append((u, aa))
    return gr


def topological_sort(g):
    ie = reverse_graph(g)

    candidates = set()
    for u in ie:
        if not ie[u]:
            candidates.add(u)

    order = []

    while candidates:
        u = candidates.pop()
        order.append(u)
        for edge in g[u]:
            v, aa = edge
            ie[v].remove((u, aa))
            if not ie[v]:
                candidates.add(v)

    return order


def decoding_ideal_spectrum(spectrum):
    graph = graph_construction(spectrum)
    order = topological_sort(graph)
    sink = order[-1]

    # building a tree
    mapping = {0: [0]}
    parent, label = [-1], ['']
    key = 0
    for u in order:
        for edge in graph[u]:
            v, aa = edge
            if v not in mapping:
                mapping[v] = []
            for i in mapping[u]:
                key += 1
                mapping[v].append(key)
                parent.append(i)
                label.append(aa)

    # walking up to source from leaves
    leaves = {i for i in mapping[sink]}
    peptides = []
    while leaves:
        i = leaves.pop()
        p = ''
        while i != -1:
            p = label[i] + p
            i = parent[i]
        peptides.append(p)

    for peptide in peptides:
        if ideal_spectrum(peptide) == spectrum:
            return peptide

    return


def main():
    spectrum = list(map(int, sys.stdin.readline().split()))
    spectrum.insert(0, 0)
    print(decoding_ideal_spectrum(spectrum))


if __name__ == '__main__':
    main()
