import sys


class Node:

    def __init__(self, key):
        self.label = key
        self.edges = {}
        self.e_lbl = {}

    def get_label(self):
        return self.label

    def change_label(self, key):
        self.label = key

    def add_edge(self, v, w):
        self.edges[v] = w
        self.e_lbl[w] = v

    def remove_edge(self, v):
        w = self.edges[v]
        self.edges.pop(v)
        self.e_lbl.pop(w)

    def edge_label(self, v):
        return self.edges[v]

    def output_edges(self):
        return self.edges.items()

    def neighbors(self):
        return self.edges.keys()

    def neighbor_by_label(self, w):
        if w in self.e_lbl:
            return self.e_lbl[w]
        else:
            return -1

    def is_leaf(self):
        return True if len(self.edges) == 0 else False


def trie_construction(patterns):
    trie = {0: Node(0)}
    cur_key = 1
    for pattern in patterns:
        cur_node = trie[0]
        for ch in pattern:
            v = cur_node.neighbor_by_label(ch)
            if v > -1:
                cur_node = trie[v]
            else:
                v = cur_key
                v_node = Node(v)
                trie[v] = v_node
                cur_node.add_edge(v, ch)
                cur_node = v_node
                cur_key += 1
    return trie


def prefix_trie_matching(text, trie):
    node = trie[0]
    i = 0
    symbol = text[i]
    while True:
        if node.is_leaf():
            return True
        v = node.neighbor_by_label(symbol)
        if v > -1:
            node = trie[v]
            i += 1
            symbol = text[i] if i < len(text) else ''
        else:
            return False


def trie_matching(text, trie):
    positions = []
    for i in range(len(text)):
        if prefix_trie_matching(text[i:], trie):
            positions.append(i)
    return positions


def main():
    text = sys.stdin.readline().strip()
    patterns = []
    for line in sys.stdin:
        patterns.append(line.strip())
    trie = trie_construction(patterns)
    print(*trie_matching(text, trie))


if __name__ == '__main__':
    main()
