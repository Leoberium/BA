import sys


def avg_distance(dm, c1, c2):
    d = 0
    for x in c1:
        for y in c2:
            d += dm[x][y]
    d /= len(c1) * len(c2)
    return d


def closest_clusters(dm, clusters):
    d_min = 10**10
    i, j = -1, -1
    for key1 in clusters:
        for key2 in clusters:
            if key1 == key2:
                continue
            d = dm[key1][key2]
            if d < d_min:
                d_min = d
                i, j = key1, key2
    return i, j


def hierarchical_clustering(data):
    # without constructing the tree
    n = len(data)
    clusters = {i: {i} for i in range(n)}
    new_clusters = []
    while len(clusters) > 1:
        # two closest clusters
        i, j = closest_clusters(data, clusters)
        ci, cj = clusters.pop(i), clusters.pop(j)
        # merging them into a new cluster
        c_new = ci.union(cj)
        # adding new row and column
        row = {}
        for key in clusters:
            c = clusters[key]
            d = avg_distance(data, c_new, c)
            row[key] = d
        for key in clusters:
            data[key][n] = row[key]
        row[n] = 0.0
        data[n] = row
        # removing rows and columns corresponding to i and j
        # no need to remove them since they are used in computing of d_avg
        # adding new cluster
        clusters[n] = c_new
        new_clusters.append(c_new)
        # updating index for next new cluster
        n += 1

    return new_clusters


def main():
    n = int(sys.stdin.readline())
    # it's better to represent distance matrix as dictionary
    dm = dict()
    for i in range(n):
        row = list(map(float, sys.stdin.readline().split()))
        dm[i] = {j: row[j] for j in range(len(row))}
    clusters = hierarchical_clustering(dm)
    for cluster in clusters:
        print(*[x + 1 for x in cluster])


if __name__ == '__main__':
    main()
