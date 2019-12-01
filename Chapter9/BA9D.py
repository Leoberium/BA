import sys

leaf_end = 0


class Node:

    def __init__(self, key):
        self.label = key
        # parent
        self.parent = None
        # children by first character of edge
        self.children = {}
        # suffix link
        self.link = None
        # start and end of the edge leading to this node
        self.start = -1
        self.end = -1
        # index of suffix (non-negative for leaves)
        self.index = -1

    def __getattribute__(self, name):
        if name == 'end':
            if self.is_leaf():
                return leaf_end
        return super().__getattribute__(name)

    def is_leaf(self):
        return True if not self.children else False

    def is_root(self):
        return True if self.parent is None else False

    def length(self):
        return self.end - self.start


def create_node(tree, key, parent, start, end):
    node = Node(key)
    tree[key] = node
    node.start = start
    node.end = end
    node.parent = parent
    return node


def suffix_tree_construction(s):
    # length of the string
    n = len(s)
    # leaf end
    global leaf_end
    # tree itself
    key = 0  # used to store the nodes by keys
    root = Node(key)
    t = {0: root}  # root has key 0
    # active point
    act_node, act_edge, act_len = root, '', 0
    # integer indicating how many new suffixes to insert
    rem = 0
    for i in range(n):
        # current character
        ch = s[i]
        # extending leaf edges
        leaf_end += 1
        # remaining suffix count
        rem += 1
        # key of last added node
        last_key = 0
        # looping through remaining suffixes
        while rem > 0:

            if act_len == 0:
                act_edge = i

            if s[act_edge] not in act_node.children:
                # creating new leaf
                key += 1
                child = create_node(tree=t, key=key, parent=act_node,
                                    start=i, end=i+1)
                act_node.children[s[act_edge]] = child
                # suffix linking
                if last_key:
                    t[last_key].link = act_node
                    last_key = 0
            else:
                next_node = act_node.children[s[act_edge]]
                # walking down
                if act_len >= next_node.length():
                    act_len -= next_node.length()
                    act_edge += next_node.length()
                    act_node = next_node
                    continue
                # if suffix already present
                if ch == s[next_node.start+act_len]:
                    # suffix linking
                    if last_key:
                        t[last_key].link = act_node
                    # active point update
                    act_len += 1
                    break
                # breaking the edge if not the whole suffix is present
                else:
                    # creating new internal node
                    key += 1
                    middle_node = create_node(
                        tree=t, key=key, parent=act_node,
                        start=next_node.start,
                        end=next_node.start+act_len
                    )
                    act_node.children[s[act_edge]] = middle_node
                    middle_node.children[s[next_node.start+act_len]] = next_node
                    # updating next node
                    next_node.parent = middle_node
                    next_node.start += act_len
                    # updating links
                    if last_key:
                        t[last_key].link = middle_node
                    last_key = key
                    # creating leaf
                    key += 1
                    leaf_node = create_node(
                        tree=t, key=key, parent=middle_node,
                        start=i, end=i+1
                    )
                    middle_node.children[ch] = leaf_node

            rem -= 1
            # updating active point
            if act_node == root and act_len > 0:
                act_len -= 1
                act_edge = i - rem + 1
            elif act_node != root and act_node.link is not None:
                act_node = act_node.link
            else:
                act_node = root

    return t


def longest_repeat(s):
    tree = suffix_tree_construction(s)
    # the deepest internal node corresponds to such substring
    root = tree[0]
    # finding all internal nodes
    internal_nodes = []
    for key in tree:
        node = tree[key]
        if node.parent is not None and node.children:
            internal_nodes.append(node)
    # computing depth of each internal node
    depth = []
    for node in internal_nodes:
        d = 0
        while node != root:
            d += node.length()
            node = node.parent
        depth.append(d)
    # finding the deepest internal node
    node = internal_nodes[depth.index(max(depth))]
    # building the substring
    r = ''
    while node != root:
        r = s[node.start:node.end] + r
        node = node.parent
    return r


def main():
    text = sys.stdin.readline().strip()
    if text[-1] != '$':
        text += '$'
    print(longest_repeat(text))


if __name__ == '__main__':
    main()
