def chromosome_to_cycle(chromosome):
    n = len(chromosome)
    nodes = [0] * 2 * n
    for j in range(n):
        i = chromosome[j]
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


def two_break_distance(p, q):
    edges = colored_edges(p) + colored_edges(q)
    blocks = sum(map(len, p))
    graph = {_+1: [] for _ in range(2 * blocks)}
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    unvisited = [1] * 2 * blocks
    # number of cycles is the same as the number of connected components for P + Q graph
    cnt = 0
    while any(unvisited):
        queue = [unvisited.index(1) + 1]
        unvisited[queue[0] - 1] = 0
        cnt += 1
        while queue:
            u = queue.pop()
            for v in graph[u]:
                if unvisited[v-1]:
                    unvisited[v-1] = 0
                    queue.append(v)

    return blocks - cnt


def main():
    genome1 = eval('[' + input().replace(' ', ', ').replace(')(', '), (') + ']')
    genome2 = eval('[' + input().replace(' ', ', ').replace(')(', '), (') + ']')
    print(two_break_distance(genome1, genome2))


if __name__ == '__main__':
    main()
