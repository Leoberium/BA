def two_break_on_genome_graph(genome_graph, i, ip, j, jp):
    for k in range(len(genome_graph)):
        edge = genome_graph[k]
        if edge == (i, ip) or edge == (ip, i):
            genome_graph[k] = (i, j)
        if edge == (j, jp) or edge == (jp, j):
            genome_graph[k] = (ip, jp)
    return genome_graph


def main():
    genome_graph = eval('[' + input() + ']')
    i, ip, j, jp = map(int, input().split(', '))
    edges = two_break_on_genome_graph(genome_graph, i, ip, j, jp)
    print(', '.join(map(str, edges)))


if __name__ == '__main__':
    main()
