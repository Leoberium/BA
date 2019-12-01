import sys
import decimal as dl


class Node:

    def __init__(self, key):
        self.edges = {}
        self.id = key

    def neighbors(self):
        return self.edges.keys()

    def degree(self):
        return len(self.edges)

    def add_edge(self, v, w):
        self.edges[v] = w

    def weight(self, v):
        if v in self.edges:
            return self.edges[v]
        else:
            return -1

    def output_edges(self):
        edges = []
        for v in self.edges:
            edges.append((v, self.edges[v]))
        return edges

    def remove_edge(self, v):
        self.edges.pop(v)

    def change_id(self, key):
        self.id = key

    def get_id(self):
        return self.id

    def is_internal(self):
        return self.degree() > 1


def attachment_point(t, i, k, x):
    unvisited = {key: 1 for key in t}
    unvisited[i] = 0
    # searching for path from i to k
    paths = {key: [i] for key in t}
    queue = [i]
    while queue:
        u = queue.pop()
        for v in t[u].neighbors():
            if unvisited[v]:
                unvisited[v] = 0
                queue.append(v)
                paths[v] = paths[u] + [v]
        if len(paths[k]) > 1:
            break
    # searching for breakpoint or node
    u, v = i, i
    for j in range(len(paths[k]) - 1):
        u, v = paths[k][j], paths[k][j+1]
        w = t[u].weight(v)
        if w > x:
            return u, v, x
        elif w == x:
            return v, v, 0
        else:
            x -= w
    return u, v, x


def nj_matrix(d):
    n = len(d)
    d_star = {i: {j: 0 for j in d[i]} for i in d}
    for i in d:
        tdi = sum(d[i].values())
        for j in d:
            if i == j:
                continue
            tdj = sum([d[k][j] for k in d])
            d_star[i][j] = (n - 2) * d[i][j] - tdi - tdj
    return d_star


def min_non_diagonal_element(d):
    i, j = -1, -1
    m = 10**10
    for key1 in d:
        for key2 in d[key1]:
            if key1 == key2:
                continue
            if d[key1][key2] < m:
                m = d[key1][key2]
                i, j = key1, key2
    return i, j


def neighbor_joining(d, n):
    # n further is used as node labeler, not number of leaves
    if len(d) == 2:
        keys = list(d.keys())
        key1, key2 = keys[0], keys[1]
        u = Node(key1)
        v = Node(key2)
        u.add_edge(key2, d[key1][key2])
        v.add_edge(key1, d[key2][key1])
        return {key1: u, key2: v}
    # neighbor-joining matrix
    d_star = nj_matrix(d)
    # its minimum non-diagonal element
    i, j = min_non_diagonal_element(d_star)
    # computing limbs
    tdi = sum(d[i].values())
    tdj = sum(d[k][j] for k in d)
    delta = (tdi - tdj) / (len(d) - 2)
    half = dl.Decimal(0.5)
    limb_i = half * (d[i][j] + delta)
    limb_j = half * (d[i][j] - delta)
    # new row and column for m (equal to current n) in distance matrix
    d[n] = {k: half * (d[k][i] + d[k][j] - d[i][j]) for k in d}
    d[n][n] = 0
    for k in d:
        if k in (i, j):
            continue
        d[k][n] = d[n][k]
    # removing i and j from distance matrix
    d.pop(i), d.pop(j)
    for k in d:
        d[k].pop(i), d[k].pop(j)
    # computing tree on new distance matrix
    t = neighbor_joining(d, n + 1)
    # adding new nodes and their limbs
    m_node = t[n]
    m_node.add_edge(i, limb_i)
    m_node.add_edge(j, limb_j)
    i_node = Node(i)
    j_node = Node(j)
    t[i], t[j] = i_node, j_node
    i_node.add_edge(n, limb_i)
    j_node.add_edge(n, limb_j)
    return t


def main():
    n = int(sys.stdin.readline())
    # distances as dictionary
    d = {}
    for i in range(n):
        row = map(dl.Decimal, sys.stdin.readline().split())
        d[i] = {j: next(row) for j in range(n)}
    tree = neighbor_joining(d, n)
    for i in range(len(tree)):
        node = tree[i]
        key = node.get_id()
        for edge in node.output_edges():
            edge = (edge[0], round(edge[1], 3))
            print(str(key) + '->' + ':'.join(map(str, edge)))


if __name__ == '__main__':
    main()
