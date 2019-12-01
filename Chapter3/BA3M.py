import sys


def one_in_one_out(g, v):
    if len(g[v]['in']) == 1 and len(g[v]['out']) == 1:
        return True
    else:
        return False


def max_non_branching_paths(g):
    paths = []
    visited = set()
    # paths
    for v in g:
        if not one_in_one_out(g, v):
            if g[v]['out']:
                for w in g[v]['out']:
                    path = [v, w]
                    while one_in_one_out(g, w):
                        u = g[w]['out'][0]
                        path.append(u)
                        w = u
                    paths.append(path)
                    for u in path:
                        visited.add(u)
    # isolated cycles
    unvisited = set(g.keys()).difference(visited)
    while unvisited:
        start = unvisited.pop()
        u = g[start]['out'][0]
        cycle = [start, u]
        while u != start:
            unvisited.remove(u)
            u = g[u]['out'][0]
            cycle.append(u)
        paths.append(cycle)
    return paths


def main():
    graph = {}
    for line in sys.stdin:
        tail, heads = line.strip().split(' -> ')
        heads = heads.split(',')
        for head in heads:
            if tail in graph:
                graph[tail]['out'].append(head)
            else:
                graph[tail] = {'in': [], 'out': [head]}
            if head in graph:
                graph[head]['in'].append(tail)
            else:
                graph[head] = {'in': [tail], 'out': []}
    paths = max_non_branching_paths(graph)
    for path in paths:
        print(' -> '.join(path))


if __name__ == '__main__':
    main()
