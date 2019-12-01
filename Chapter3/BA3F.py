import sys


def are_unexplored_edges(ue):
    flag = False
    for u in ue:
        if ue[u]:
            flag = True
    return flag


def random_walk(start, al, ue):
    # cyclic walk
    cycle = [start]
    v = start
    while True:
        u = cycle[-1]
        for i in range(len(al[u])):
            if i in ue[u]:
                v = al[u][i]
                ue[u].remove(i)
                cycle.append(v)
                break
        if v == start:
            break
    return cycle


def eulerian_cycle(adj_list):
    start = min(adj_list.keys())
    unexplored_edges = {u: set(range(len(adj_list[u]))) for u in adj_list}
    # initial cycle
    cycle = random_walk(start, adj_list, unexplored_edges)
    while are_unexplored_edges(unexplored_edges):
        for i in range(len(cycle)):
            u = cycle[i]
            if unexplored_edges[u]:
                start = u
                new_cycle = random_walk(start, adj_list, unexplored_edges)
                cycle = cycle[:i] + new_cycle + cycle[i+1:]
    return cycle


def main():
    adj_list = dict()
    for line in sys.stdin:
        line = line.strip()
        tail, head = line.split(' -> ')
        adj_list[int(tail)] = list(map(int, head.split(',')))
    cycle = eulerian_cycle(adj_list)
    print('->'.join(map(str, cycle)))


if __name__ == '__main__':
    main()
