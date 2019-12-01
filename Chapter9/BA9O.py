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


class StringThing:

    def __init__(self, s):
        self.s = s if s[-1] == '$' else s + '$'
        self.array = []
        self.tree = {}
        self.suffix_tree_construction()
        # special dictionaries for DFS
        self.path = {node: False for node in self.tree.values()}
        self.visited = {node: 0 for node in self.tree.values()}
        self.depth_first_traversal(self.tree[0])
        # bwt things
        self.t = ''.join([self.s[x-1] for x in self.array])
        self.n = len(self.t)
        self.last = list(self.t)
        self.first = sorted(self.last)
        self.counts = {ch: [0] * self.n for ch in set(self.last)}
        self.compute_counts_array()
        self.first_occurrence = {ch: self.first.index(ch) for ch in set(self.last)}
        self.lft = [-1] * self.n
        self.compute_last_to_first()

    def approximate_pattern_matching(self, pattern, d):
        # suffix array is needed to know the positions
        # that's why this complicated class with suffix tree and array
        pattern = list(pattern)
        # accumulated mismatches for each start position
        mismatches = [0] * self.n
        # mapping between last and first
        mapping = {pos: pos for pos in range(self.n)}
        # start positions of last
        bwt_pos = {pos for pos in range(self.n)}
        while pattern:
            ch = pattern.pop()
            # counting mismatches
            for pos in bwt_pos:
                if ch != self.last[mapping[pos]]:
                    mismatches[pos] += 1
            # filtering positions
            for pos in bwt_pos.copy():
                if mismatches[pos] > d:
                    bwt_pos.remove(pos)
            # updating indices
            mapping = {
                key: self.lft[value] for key, value
                in mapping.copy().items() if key in bwt_pos
            }
        return [self.array[mapping[pos]] for pos in bwt_pos]

    def compute_last_to_first(self):
        for i in range(self.n):
            ch = self.last[i]
            left, right = 0, self.n - 1

            while left < right:
                mid = (left + right) // 2
                if self.first[mid] < ch:
                    left = mid + 1
                else:
                    right = mid

            self.lft[i] = left + self.counts[ch][i] - 1

    def compute_counts_array(self):
        self.counts[self.last[0]][0] = 1
        for i in range(1, self.n):
            ch = self.last[i]
            for symbol in self.counts:
                if ch == symbol:
                    self.counts[symbol][i] = self.counts[symbol][i - 1] + 1
                else:
                    self.counts[symbol][i] = self.counts[symbol][i - 1]

    def pattern_matching_with_suffix_array(self, pattern):
        left, right = 0, len(self.array) - 1
        n = len(self.s)  # length of text
        m = len(pattern)  # length of pattern
        while left < right:
            mid = (left + right) // 2
            pos = self.array[mid]  # position of mid suffix in text
            if pattern > self.s[pos:min(pos+m, n)]:
                left = mid + 1
            else:
                right = mid
        first = left
        right = len(self.array) - 1
        while left < right:
            mid = (left + right) // 2
            pos = self.array[mid]  # position of mid suffix in text
            if pattern < self.s[pos:min(pos+m, n)]:
                right = mid
            else:
                left = mid + 1
        last = right
        if first > last:
            return []
        else:
            return self.array[first:last]

    def partial_suffix_array(self, k):
        return [(i, pos) for i, pos in enumerate(self.array) if pos % k == 0]

    def depth_first_traversal(self, node):
        # visiting
        self.visited[node] = True
        # updating path
        if node.parent is not None:
            self.path[node] = self.path[node.parent] + node.length()
        # index if leaf
        if node.is_leaf():
            node.index = len(self.s) - self.path[node]
            self.array.append(node.index)
            return
        order = sorted(node.children.keys())
        for v in order:
            child = node.children[v]
            if not self.visited[child]:
                self.depth_first_traversal(child)

    def create_node(self, key, parent, start, end):
        node = Node(key)
        self.tree[key] = node
        node.start = start
        node.end = end
        node.parent = parent
        return node

    def suffix_tree_construction(self):
        # length of the string
        n = len(self.s)
        # leaf end
        global leaf_end
        # tree itself
        key = 0  # used to store the nodes by keys
        root = Node(key)
        self.tree[key] = root
        # active point
        act_node, act_edge, act_len = root, '', 0
        # integer indicating how many new suffixes to insert
        rem = 0
        for i in range(n):
            # current character
            ch = self.s[i]
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

                if self.s[act_edge] not in act_node.children:
                    # creating new leaf
                    key += 1
                    child = self.create_node(key=key, parent=act_node,
                                             start=i, end=i + 1)
                    act_node.children[self.s[act_edge]] = child
                    # suffix linking
                    if last_key:
                        self.tree[last_key].link = act_node
                        last_key = 0
                else:
                    next_node = act_node.children[self.s[act_edge]]
                    # walking down
                    if act_len >= next_node.length():
                        act_len -= next_node.length()
                        act_edge += next_node.length()
                        act_node = next_node
                        continue
                    # if suffix already present
                    if ch == self.s[next_node.start + act_len]:
                        # suffix linking
                        if last_key:
                            self.tree[last_key].link = act_node
                        # active point update
                        act_len += 1
                        break
                    # breaking the edge if not the whole suffix is present
                    else:
                        # creating new internal node
                        key += 1
                        middle_node = self.create_node(
                            key=key, parent=act_node,
                            start=next_node.start,
                            end=next_node.start + act_len
                        )
                        act_node.children[self.s[act_edge]] = middle_node
                        middle_node.children[self.s[next_node.start + act_len]] = next_node
                        # updating next node
                        next_node.parent = middle_node
                        next_node.start += act_len
                        # updating links
                        if last_key:
                            self.tree[last_key].link = middle_node
                        last_key = key
                        # creating leaf
                        key += 1
                        leaf_node = self.create_node(
                            key=key, parent=middle_node,
                            start=i, end=i + 1
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


def main():
    sa = StringThing(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    d = int(sys.stdin.readline())
    positions = []
    for pattern in patterns:
        positions += sa.approximate_pattern_matching(pattern, d)
    print(*positions)


if __name__ == '__main__':
    main()
