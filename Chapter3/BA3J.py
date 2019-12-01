import sys


def find_start(al):
    for u in al:
        out_degree = len(al[u])
        in_degree = 0
        for v in al:
            in_degree += al[v].count(u)
        if in_degree + out_degree % 2 == 1:
            return u


def are_unexplored_edges(ue):
    flag = False
    for u in ue:
        if ue[u]:
            flag = True
    return flag


def random_path_walk(start, al, ue):
    # path walk
    path = [start]
    while True:
        u = path[-1]
        if u not in al:
            break
        for i in range(len(al[u])):
            if i in ue[u]:
                v = al[u][i]
                if v == start:
                    continue
                ue[u].remove(i)
                path.append(v)
                break
        if path[-1] == u:
            break
    return path


def random_cycle_walk(start, al, ue):
    # cyclic walk
    cycle = [start]
    while True:
        u = cycle[-1]
        if u not in al:
            break
        for i in range(len(al[u])):
            if i in ue[u]:
                v = al[u][i]
                ue[u].remove(i)
                cycle.append(v)
                break
        if cycle[-1] == start:
            break
    return cycle


def eulerian_path(adj_list):
    start = find_start(adj_list)
    unexplored_edges = {u: set(range(len(adj_list[u]))) for u in adj_list}
    # initial path
    path = random_path_walk(start, adj_list, unexplored_edges)
    while are_unexplored_edges(unexplored_edges):
        for i in range(len(path)):
            u = path[i]
            if u not in adj_list:
                continue
            if unexplored_edges[u]:
                cycle = random_cycle_walk(u, adj_list, unexplored_edges)
                path = path[:i] + cycle + path[i+1:]
    return path


def paired_string_reconstruction(pc, k, d):
    graph = {}
    for pair in pc:
        prefix = (pair[0][:k-1], pair[1][:k-1])
        suffix = (pair[0][1:], pair[1][1:])
        if prefix in graph:
            graph[prefix].append(suffix)
        else:
            graph[prefix] = [suffix]
    path = eulerian_path(graph)
    string1, string2 = '', ''
    for pair in path:
        read1, read2 = pair
        string1 += read1[-1] if string1 else read1[:(k-1)]
        string2 += read2[-1] if string2 else read2[:(k-1)]
    string = string1 + string2[-(k+d):]
    return string


def main():
    k, d = map(int, sys.stdin.readline().split())
    paired_reads = []
    for line in sys.stdin:
        line = line.strip()
        read1, read2 = line.split('|')
        paired_reads.append((read1, read2))
    ans = paired_string_reconstruction(paired_reads, k, d)
    print(ans)


if __name__ == '__main__':
    main()
