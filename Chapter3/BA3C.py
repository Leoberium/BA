import sys


def prefix(string):
    k = len(string)
    return string[:k-1]


def suffix(string):
    k = len(string)
    return string[-k+1:]


def overlap_graph(dna):
    k = len(dna[0])
    edges = []
    for s1 in dna:
        for s2 in dna:
            if suffix(s1) == prefix(s2):
                edges.append((s1, s2))
    return edges


def main():
    dna = []
    for line in sys.stdin:
        line = line.strip()
        dna.append(line)
    edges = overlap_graph(dna)
    for edge in edges:
        tail, head = edge
        print(tail, '->', head)


if __name__ == '__main__':
    main()
