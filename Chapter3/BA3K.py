import sys


def one_in_one_out(u):
    return True if len(u['in']) == 1 and len(u['out']) == 1 else False


def contigs_generation(reads):
    k = len(reads[0])
    c = []
    # graph generation
    graph = {}
    for read in reads:
        prefix = read[:(k-1)]
        suffix = read[1:]
        if prefix in graph:
            graph[prefix]['out'].append(suffix)
        else:
            graph[prefix] = {'in': [], 'out': [suffix]}
        if suffix in graph:
            graph[suffix]['in'].append(prefix)
        else:
            graph[suffix] = {'in': [prefix], 'out': []}
    # contigs
    for u in graph:
        if not one_in_one_out(graph[u]):
            if graph[u]['out']:
                for v in graph[u]['out']:
                    contig = u + v[-1]
                    while one_in_one_out(graph[v]):
                        v = graph[v]['out'][0]
                        contig += v[-1]
                    c.append(contig)
    return c


def main():
    patterns = []
    for line in sys.stdin:
        patterns.append(line.strip())
    print(*contigs_generation(reads=patterns))


if __name__ == '__main__':
    main()
