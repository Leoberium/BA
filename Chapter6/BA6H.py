def chromosome_to_cycle(chromosome):
    n = len(chromosome)
    nodes = [0] * 2 * n
    for j in range(n):
        i = int(chromosome[j])
        if i > 0:
            nodes[2 * j] = 2 * i - 1
            nodes[2 * j + 1] = 2 * i
        else:
            nodes[2 * j] = -2 * i
            nodes[2 * j + 1] = -2 * i - 1
    return nodes


def colored_edges(p):
    edges = []
    for chromosome in p:
        nodes = chromosome_to_cycle(chromosome)
        nodes.append(nodes[0])
        for i in range(len(chromosome)):
            edge = (nodes[2*i+1], nodes[2*i+2])
            edges.append(edge)
    return edges


def main():
    p = input().split(')(')
    p[0], p[-1] = p[0][1:], p[-1][:-1]
    p = list(map(lambda x: x.split(), p))
    c = list(map(str, colored_edges(p)))
    print(', '.join(c))


if __name__ == '__main__':
    main()
