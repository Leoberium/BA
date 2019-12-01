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
    return chromosome


def two_break_on_genome(p, i, ip, j, jp):
    nodes = chromosome_to_cycle(p)
    nodes.append(nodes[0])
    # adjacency list for graph
    adj_list = {nodes[0]: [0, 0]}
    for k in range(len(nodes) - 1):
        u, v = nodes[k], nodes[k+1]
        adj_list[u][1] = v
        if v in adj_list:
            adj_list[v][0] = u
        else:
            adj_list[v] = [u, 0]
    # rewiring
    index = adj_list[i].index(ip)
    adj_list[i][index] = j
    index = adj_list[j].index(jp)
    adj_list[j][index] = i
    index = adj_list[ip].index(i)
    adj_list[ip][index] = jp
    index = adj_list[jp].index(j)
    adj_list[jp][index] = ip
    unvisited = [1] * len(adj_list)
    # searching for cycles
    cycles = []
    while any(unvisited):
        start = unvisited.index(1) + 1
        cycle = [start]
        unvisited[start-1] = 0
        while adj_list[cycle[-1]][1] != start:
            f = adj_list[cycle[-1]][1]
            unvisited[f-1] = 0
            cycle.append(f)
        cycle.append(adj_list[cycle[-1]][1])
        if abs(cycle[1] - cycle[0]) == 1:
            cycles.append(cycle[:-1])
        else:
            cycles.append(cycle[1:])
    genome = []
    for cycle in cycles:
        genome.append('(' + ' '.join(cycle_to_chromosome(cycle)) + ')')
    return genome


def main():
    p = eval(input().replace(' ', ', '))
    i, ip, j, jp = map(int, input().split(', '))
    print(' '.join(two_break_on_genome(p, i, ip, j, jp)))


if __name__ == '__main__':
    main()
