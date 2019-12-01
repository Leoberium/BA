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


def cycle_to_chromosome(nodes):
    n = len(nodes)
    chromosome = []
    for i in range(0, n, 2):
        p1, p2 = nodes[i], nodes[i+1]
        if p1 < p2:
            chromosome.append('+' + str(p2 // 2))
        else:
            chromosome.append('-' + str(p1 // 2))
    return tuple(chromosome)


def colored_edges(p):
    edges = []
    for chromosome in p:
        nodes = chromosome_to_cycle(chromosome)
        nodes.append(nodes[0])
        for i in range(len(chromosome)):
            edge = {nodes[2*i+1], nodes[2*i+2]}
            edges.append(edge)
    return edges


def cc(g):
    # number of connected components
    unvisited = [1] * len(g)
    cnt = 0
    while any(unvisited):
        queue = [unvisited.index(1) + 1]
        unvisited[queue[0] - 1] = 0
        cnt += 1
        while queue:
            u = queue.pop()
            for v in g[u]:
                if unvisited[v - 1]:
                    unvisited[v - 1] = 0
                    queue.append(v)
    return cnt


def edges_to_genome(edges):
    n = len(edges)
    graph = {i: [(i - 1, i + 1)[i % 2]] for i in range(1, 2 * n + 1)}
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    unvisited = [1] * (2 * n)
    cycles = []
    while any(unvisited):
        start = unvisited.index(1) + 1
        unvisited[start-1] = 0
        cycle = [start]
        while True:
            u = cycle[-1]
            flag = True
            for v in graph[u]:
                if unvisited[v-1]:
                    unvisited[v-1] = 0
                    cycle.append(v)
                    flag = False
                    break
            if flag:
                break
        cycles.append(cycle)

    genome = []

    for cycle in cycles:
        genome.append(cycle_to_chromosome(cycle))

    return genome


def two_break_sorting(p, q):
    permutations = [p]

    red_edges = colored_edges(p)
    blue_edges = colored_edges(q)
    blocks = sum(map(len, p))

    # breakpoint graph
    graph = {_+1: [] for _ in range(2 * blocks)}
    for edge in blue_edges + red_edges:
        u, v = edge
        # 0 - back, 1 - forward
        if v not in graph[u]:
            graph[u].append(v)
        elif len(graph[u]) < 2:
            graph[u].append(v)
        if u not in graph[v]:
            graph[v].append(u)
        elif len(graph[v]) < 2:
            graph[v].append(u)

    while cc(graph) < blocks:
        b1, b2, r1, r2 = -1, -1, -1, -1
        # arbitrary blue edge
        for edge in blue_edges:
            u, v = edge
            if graph[u].count(v) < 2:
                b1, b2 = u, v
                break

        # updating the graph
        graph[b1].remove(b2)
        r1 = graph[b1].pop()
        graph[b1] += [b2, b2]

        graph[b2].remove(b1)
        r2 = graph[b2].pop()
        graph[b2] += [b1, b1]

        graph[r1].remove(b1)
        graph[r1].append(r2)
        graph[r2].remove(b2)
        graph[r2].append(r1)

        red_edges.remove({b1, r1})
        red_edges.remove({b2, r2})
        red_edges.append({b1, b2})
        red_edges.append({r1, r2})

        p = edges_to_genome(red_edges)

        permutations.append(p)

    return permutations


def main():
    genome1 = [tuple(input().strip('()').split())]
    genome2 = [tuple(input().strip('()').split())]
    for genome in two_break_sorting(genome1, genome2):
        string = ''
        for chromosome in genome:
            string += '(' + ' '.join(chromosome) + ')'
        print(string)


if __name__ == '__main__':
    main()
