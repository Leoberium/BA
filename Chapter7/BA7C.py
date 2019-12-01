import sys


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


def limb(d, leaf):
    n = len(d)
    limb_min = max(d[0])
    for j in range(n):
        if j == leaf:
            continue
        for k in range(j, n):
            if k == leaf:
                continue
            c = (d[leaf][j] + d[leaf][k] - d[j][k]) // 2
            if c < limb_min:
                limb_min = c
    return limb_min


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


def additive_phylogeny(d, n, p):
    # p - current number of leaves
    # n - total number of leaves
    if p == 2:
        x = Node(0)
        y = Node(1)
        x.add_edge(1, d[0][1])
        y.add_edge(0, d[1][0])
        return {0: x, 1: y}
    p -= 1  # using it as index
    # bald distance matrix
    limb_length = limb(d, p)
    for j in range(p):
        d[j][p] -= limb_length
        d[p][j] -= limb_length
    # getting leaves
    leaves = (-1, -1, -1)
    for i in range(p):
        for k in range(p):
            if d[i][k] == d[i][p] + d[p][k]:
                leaves = (i, p, k)
                break
    i, p, k = leaves
    x = d[i][p]
    # trimming distance matrix
    d.pop()
    for j in range(p):
        d[j].pop()
    # recursion
    t = additive_phylogeny(d, n, p)
    # searching for the attachment point
    u, v, x = attachment_point(t, i, k, x)
    # creating the attachment point
    if x == 0:
        v_node = t[v]
        key = v_node.get_id()
        # special case when one of the initial lives is used as an internal node
        if p == 2:
            key = n
            v_node.change_id(key)
    else:
        # how many internal nodes already
        # to know the key to assign to a new internal node
        cnt = 0
        for node in t.values():
            if node.is_internal():
                cnt += 1
        key = n + cnt
        # new node
        v_node = Node(key)
        v_node.add_edge(u, x)
        v_node.add_edge(v, t[u].weight(v) - x)
        # rewiring
        t[u].remove_edge(v)
        t[v].remove_edge(u)
        t[u].add_edge(key, x)
        t[v].add_edge(key, v_node.weight(v))
        # adding new node
        t[key] = v_node
    v_node.add_edge(p, limb_length)
    leaf_node = Node(p)
    leaf_node.add_edge(key, limb_length)
    t[p] = leaf_node

    return t


def main():
    n = int(sys.stdin.readline())
    d = []
    for _ in range(n):
        d.append(list(map(int, sys.stdin.readline().split())))
    tree = additive_phylogeny(d, n, n)
    for i in range(len(tree)):
        node = tree[i]
        key = node.get_id()
        for edge in node.output_edges():
            print(str(key) + '->' + ':'.join(map(str, edge)))


if __name__ == '__main__':
    main()
