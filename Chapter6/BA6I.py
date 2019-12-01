def cycle_to_chromosome(nodes):
    n = len(nodes)
    chromosome = []
    for i in range(0, n, 2):
        p1, p2 = nodes[i], nodes[i+1]
        if p1 < p2:
            chromosome.append('+' + str(p2 // 2))
        else:
            chromosome.append('-' + str(p1 // 2))
    return chromosome


def graph_to_genome(genome_graph):
    p = ''
    nodes = []
    for edge in genome_graph:
        adj_left = edge[0] + 1 if edge[0] % 2 == 1 else edge[0] - 1
        nodes += [adj_left, edge[0]]
        if nodes[0] == edge[1]:
            p += '(' + ' '.join(cycle_to_chromosome(nodes)) + ')'
            nodes = []
    return p


def main():
    genome_graph = eval('[' + input() + ']')
    print(graph_to_genome(genome_graph))


if __name__ == '__main__':
    main()
