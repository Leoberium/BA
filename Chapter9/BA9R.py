import sys


def suffix_tree_construction(text, sa, lcp):
    assert len(sa) == len(lcp)
    n = len(sa)
    key, root = 0, 0
    children, parent = {root: {}}, {root: None}
    start, length = {root: -1}, {root: -1}
    depth = {0: 0}
    # active node
    act_node = root
    for i in range(n):
        while depth[act_node] > lcp[i]:
            act_node = parent[act_node]
        if depth[act_node] == lcp[i]:
            # creating a new leaf
            key += 1
            parent[key] = act_node
            children[act_node].update({text[sa[i] + lcp[i]]: key})
            start[key] = sa[i] + lcp[i]
            length[key] = n - start[key]
            depth[key] = lcp[i] + length[key]
            act_node = key
        else:
            edge_pos = lcp[i] - depth[act_node]
            ch = text[sa[i] + depth[act_node]]
            # breaking the edge
            next_node = children[act_node][ch]
            key += 1  # new internal node
            int_node = key
            parent[key] = act_node
            children[act_node][ch] = key
            start[key] = start[next_node]
            length[key] = edge_pos
            depth[key] = depth[act_node] + edge_pos
            # rewiring
            parent[next_node] = key
            start[next_node] = start[next_node] + edge_pos
            length[next_node] = length[next_node] - edge_pos
            # new leaf
            key += 1
            ch = text[sa[i] + depth[act_node] + edge_pos]
            parent[key] = int_node
            children[int_node] = {ch: key}
            start[key] = sa[i] + depth[act_node] + edge_pos
            length[key] = n - start[key]
            depth[key] = depth[int_node] + length[key]
            act_node = key

    edges = []
    for key in start:
        if key == root:
            continue
        edges.append((start[key], length[key]))

    return edges


def main():
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().split(', ')))
    lcp = list(map(int, sys.stdin.readline().split(', ')))
    for start, length in suffix_tree_construction(text, sa, lcp):
        print(text[start:start+length])


if __name__ == '__main__':
    main()
