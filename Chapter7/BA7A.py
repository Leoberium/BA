import sys


def distances_between_leaves(tree, n):
    a = []
    leaves = []
    for node in tree:
        if len(tree[node]) == 1:
            leaves.append(node)
    assert len(leaves) == n
    for leaf in leaves:
        queue = [leaf]
        path = [0] * len(tree)
        visited = [0] * len(tree)
        visited[leaf] = 1
        while queue:
            cur = queue.pop()
            for v, w in tree[cur]:
                if not visited[v]:
                    path[v] = path[cur] + w
                    visited[v] = 1
                    queue.append(v)
        a.append([path[u] for u in leaves])
    return a


def main():
    n = int(sys.stdin.readline())
    tree = {}
    for line in sys.stdin:
        line = line.strip()
        line = line.split('->')
        u = int(line[0])
        v, w = map(int, line[1].split(':'))
        if u not in tree:
            tree[u] = [(v, w)]
        else:
            tree[u].append((v, w))
    for row in distances_between_leaves(tree, n):
        print(*row)


if __name__ == '__main__':
    main()
