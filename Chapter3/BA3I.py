def generate_kmers(a, k):
    if k == 1:
        for ch in a:
            yield ch
    else:
        for ch in a:
            for s in generate_kmers(a, k - 1):
                yield ch + s


def cyclic_walk(start, a, ue):
    c = [start]
    while True:
        u = c[-1]
        n = len(a[u])
        if not any(ue[u]):
            break
        for i in range(n):
            if ue[u][i] == 1:
                v = a[u][i]
                c.append(v)
                ue[u][i] = 0
                break
    return c


def universal_circular_string(a, k):
    adj_dict = {}
    for k_mer in generate_kmers(a, k):
        prefix = k_mer[:(k-1)]
        suffix = k_mer[1:]
        if prefix in adj_dict:
            adj_dict[prefix].append(suffix)
        else:
            adj_dict[prefix] = [suffix]
    # now eulerian cycle
    ue = {u: [1] * len(adj_dict[u])  for u in adj_dict}
    start = list(adj_dict.keys())[0]
    cycle = cyclic_walk(start, adj_dict, ue)
    flag = True
    while flag:
        flag = False
        for i in range(len(cycle)):
            u = cycle[i]
            if any(ue[u]):
                flag = True
                new_cycle = cyclic_walk(u, adj_dict, ue)
                cycle = cycle[:i] + new_cycle + cycle[i+1:]
                break
    string = cycle[0]
    n = len(cycle)
    for i in range(1, n - k + 1):
        string += cycle[i][-1]
    return string


def main():
    k = int(input())
    alphabet = ['0', '1']
    print(universal_circular_string(alphabet, k))



if __name__ == '__main__':
    main()
