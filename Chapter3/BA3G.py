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


def main():
    adj_list = dict()
    for line in sys.stdin:
        line = line.strip()
        tail, head = line.split(' -> ')
        adj_list[int(tail)] = list(map(int, head.split(',')))
    path = eulerian_path(adj_list)
    print('->'.join(map(str, path)))


if __name__ == '__main__':
    main()
