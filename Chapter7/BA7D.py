import sys


class Node:

    def __init__(self, key):
        self.edges = {}
        self.id = key
        self.age = 0

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

    def change_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def is_internal(self):
        return self.degree() > 1


def closest_clusters(clusters, d):
    i, j = -1, -1
    min_dist = 10**10
    for key1 in clusters:
        for key2 in clusters:
            if key2 == key1:
                continue
            dist = 0
            c1, c2 = clusters[key1], clusters[key2]
            for u in c1:
                for v in c2:
                    dist += d[u][v]
            dist /= len(c1) * len(c2)
            if dist < min_dist:
                i, j = key1, key2
                min_dist = dist
    return i, j, min_dist


def upgma(d, n):
    t = {leaf: Node(leaf) for leaf in range(n)}
    clusters = {leaf: {leaf} for leaf in range(n)}
    # representing distance matrix to dictionary
    # to simplify working with labels
    distances = dict()
    for i in range(n):
        distances[i] = {}
        for j in range(n):
            distances[i][j] = d[i][j]

    while len(clusters) > 1:
        # two closest clusters by keys (labels)
        i, j, dist = closest_clusters(clusters, d)
        c1, c2 = clusters[i], clusters[j]
        # new cluster
        c_new = c1.union(c2)
        clusters[n] = c_new
        # new node
        v_node = Node(n)
        v_node.change_age(dist / 2)
        t[n] = v_node
        # adding edges
        wi = round(v_node.get_age() - t[i].get_age(), 3)
        wj = round(v_node.get_age() - t[j].get_age(), 3)
        v_node.add_edge(i, wi)
        v_node.add_edge(j, wj)
        t[i].add_edge(n, wi)
        t[j].add_edge(n, wj)
        # adding row and column for c_new to distance matrix
        row = dict()
        for key in distances:
            if key == i or key == j:
                continue
            dist = (distances[key][i] + distances[key][j]) / 2
            distances[key][n] = dist
            row[key] = dist
        row[n] = 0
        distances[n] = row
        # removing rows and columns of c1 and c2 from distance matrix
        distances.pop(i)
        distances.pop(j)
        for key in distances:
            if key == n:
                continue
            distances[key].pop(j)
            distances[key].pop(i)
        # removing c1 and c2 from clusters
        clusters.pop(i), clusters.pop(j)
        n += 1

    return t


def main():
    n = int(sys.stdin.readline())
    d = []
    for _ in range(n):
        d.append(list(map(int, sys.stdin.readline().split())))
    tree = upgma(d, n)
    for i in range(len(tree)):
        node = tree[i]
        key = node.get_id()
        for edge in node.output_edges():
            print(str(key) + '->' + ':'.join(map(str, edge)))


if __name__ == '__main__':
    main()
