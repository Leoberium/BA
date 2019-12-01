import sys


def topological_ordering(g):
    order = []
    candidates = set()
    for node in g:
        if not g[node]['in']:
            candidates.add(node)

    while candidates:
        u = candidates.pop()
        order.append(u)
        for v in g[u]['out'].copy():
            g[u]['out'].remove(v)
            g[v]['in'].remove(u)
            if not g[v]['in']:
                candidates.add(v)

    return order


def main():
    graph = {}
    for line in sys.stdin:
        tail, heads = line.split(' -> ')
        tail = int(tail)
        heads = map(int, heads.split(','))
        for head in heads:
            if tail not in graph:
                graph[tail] = {'out': {head}, 'in': set()}
            else:
                graph[tail]['out'].add(head)
            if head not in graph:
                graph[head] = {'out': set(), 'in': {tail}}
            else:
                graph[head]['in'].add(tail)
    print(', '.join(map(str, topological_ordering(graph))))


if __name__ == '__main__':
    main()
