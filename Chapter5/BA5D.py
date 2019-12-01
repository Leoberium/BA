import sys


def topological_ordering(g):
    order = []
    candidates = set()

    gc = {}

    # full copy
    for node in g:
        gc[node] = {key: value.copy() for key, value in g[node].items()}

    for node in gc:
        if not gc[node]['in']:
            candidates.add(node)

    while candidates:
        u = candidates.pop()
        order.append(u)
        for e in gc[u]['out'].copy():
            u, v, w = e
            gc[u]['out'].remove(e)
            gc[v]['in'].remove(e)
            if not gc[v]['in']:
                candidates.add(v)

    for node in gc:
        if gc[node]['in'] or gc[node]['out']:
            return -1

    return order


def longest_path_in_dag(g, source, sink):
    s = [-10**10] * len(g)
    order = topological_ordering(g)
    s[source] = 0

    for node in order:
        t = []
        if not g[node]['in']:
            continue
        for e in g[node]['in']:
            u, v, w = e
            t.append(s[int(u)] + w)
        s[node] = max(t)

    p = sink
    path = [p]
    while p != source:
        for e in g[p]['in']:
            u, v, w = e
            if s[u] + w == s[p]:
                p = u
                path.append(p)
                break

    return s[sink], path[::-1]


def main():
    source = int(sys.stdin.readline())
    sink = int(sys.stdin.readline())
    graph = {_: {'in': set(), 'out': set()} for _ in range(sink + 1)}
    for line in sys.stdin:
        line = line.strip()
        tail, head_weight = line.split('->')
        head, weight = head_weight.split(':')
        tail, head, weight = map(int, [tail, head, weight])
        if tail not in graph:
            graph[tail] = {'in': set(), 'out': {(tail, head, weight)}}
        else:
            graph[tail]['out'].add((tail, head, weight))
        if head not in graph:
            graph[head] = {'in': {(tail, head, weight)}, 'out': set()}
        else:
            graph[head]['in'].add((tail, head, weight))
    result = longest_path_in_dag(graph, source, sink)
    print(result[0])
    print('->'.join(map(str, result[1])))


if __name__ == '__main__':
    main()
