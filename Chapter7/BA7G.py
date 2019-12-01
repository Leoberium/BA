import sys


alpha = ['A', 'C', 'G', 'T']
loa = len(alpha)


class Node:

    def __init__(self, key, leaf=False):
        self.id = key
        self.label = ''
        self.leaf = leaf
        self.edges = {}

    def is_leaf(self):
        return self.leaf

    def get_label(self):
        return self.label

    def add_label(self, label):
        self.label += label

    def children(self):
        return [v for v in self.edges if v < self.id]

    def add_edge(self, v, w):
        self.edges[v] = w

    def get_weight(self, v):
        return self.edges[v]

    def change_weight(self, v, w):
        self.edges[v] = w

    def add_weight(self, v, dw):
        self.edges[v] += dw

    def remove_edge(self, v):
        self.edges.pop(v)

    def output_edges(self):
        return self.edges.items()


def ripe_node(t, tag):
    for v in range(len(tag)):
        if tag[v] == 1:
            continue
        node = t[v]
        if all([tag[child] for child in node.children()]):
            return v
    return 0


def small_parsimony(t, character):
    tag = [0] * len(t)
    s = [[0] * 4 for _ in range(len(t))]
    for v in t:
        if t[v].is_leaf():
            tag[v] = 1
            for i in range(loa):
                ch = alpha[i]
                if character[v] != ch:
                    s[v][i] = 10**10

    while ripe_node(t, tag):
        v = ripe_node(t, tag)
        tag[v] = 1
        daughter, son = t[v].children()
        for i in range(loa):
            ch = alpha[i]
            min_daughter = min([s[daughter][j] + (alpha[j] != ch) for j in range(loa)])
            min_son = min([s[son][j] + (alpha[j] != ch) for j in range(loa)])
            s[v][i] = min_daughter + min_son
    return s


def parsimony_unrooted(t, n):
    # rooting
    root = max(t.keys()) + 1
    root_node = Node(root)
    t[root] = root_node
    u, v = root - 1, root - 2
    u_node, v_node = t[u], t[v]
    root_node.add_edge(u, 0)
    root_node.add_edge(v, 0)
    u_node.remove_edge(v)
    u_node.add_edge(root, 0)
    v_node.remove_edge(u)
    v_node.add_edge(root, 0)
    # length of dna string
    k = len(t[0].get_label())
    score = 0
    # looping through characters of dna strings
    for j in range(k):
        # calculating scores
        character = [t[i].get_label()[j] for i in range(n)]
        s = small_parsimony(t, character)
        min_score = min(s[-1])
        score += min_score
        # assigning label to root
        ch = alpha[s[-1].index(min_score)]
        t[root].add_label(ch)
        # backtracking through internal nodes
        stack = [(root, ch)]
        visited = [i < n for i in range(len(t))]
        while stack:
            u, u_ch = stack.pop()
            children = t[u].children()
            for v in children:
                transition = [s[v][j] + (alpha[j] != u_ch) for j in range(loa)]
                index = transition.index(min(transition))
                v_ch = alpha[index]
                dw = int(u_ch != v_ch)
                t[u].add_weight(v, dw)
                t[v].add_weight(u, dw)
                # in case if not visited or not leaf
                if not visited[v]:
                    visited[v] = 1
                    stack.append((v, v_ch))
                    t[v].add_label(v_ch)
    # removing the root
    u, v = root - 1, root - 2
    u_w = root_node.get_weight(u)
    v_w = root_node.get_weight(v)
    t.pop(root)
    root_node.remove_edge(u)
    root_node.remove_edge(v)
    u_node.remove_edge(root)
    u_node.add_edge(v, u_w + v_w)
    v_node.remove_edge(root)
    v_node.add_edge(u, u_w + v_w)

    return score, t


def main():
    n = int(sys.stdin.readline())
    tree = {key: Node(key, leaf=True) for key in range(n)}
    c = 0
    # tree parsing
    for line in sys.stdin:
        u, v = line.strip().split('->')
        if u.isalpha():
            # u is a label
            v = int(v)
            if v not in tree:
                internal_node = Node(v)
                tree[v] = internal_node
            tree[c].add_label(u)
            tree[c].add_edge(v, 0)
        elif v.isalpha():
            # v is a label
            u = int(u)
            if u not in tree:
                internal_node = Node(u)
                tree[u] = internal_node
            tree[u].add_edge(c, 0)
            c += 1
        else:
            u, v = map(int, (u, v))
            if u not in tree:
                internal_node = Node(u)
                tree[u] = internal_node
            if v not in tree:
                internal_node = Node(v)
                tree[v] = internal_node
            tree[u].add_edge(v, 0)
    # computation
    score, tree = parsimony_unrooted(tree, n)
    print(score)
    for u in tree:
        u_node = tree[u]
        u_label = u_node.get_label()
        for v, w in u_node.output_edges():
            v_node = tree[v]
            v_label = v_node.get_label()
            print(u_label + '->' + v_label + ':' + str(w))


if __name__ == '__main__':
    main()
