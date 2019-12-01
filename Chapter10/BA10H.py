import sys


def parameters(x, alphabet, path, states):
    alphabet, path = list(alphabet), list(path)
    transition = {state: {state: 0 for state in states} for state in states}
    emission = {state: {ch: 0 for ch in alphabet} for state in states}
    # counting
    emission[path[0]][x[0]] += 1
    for i in range(1, len(path)):
        prev, cur = path[i-1], path[i]
        transition[prev][cur] += 1
        emission[cur][x[i]] += 1
    # normalization
    for state in states:
        t_row = transition[state]
        e_row = emission[state]
        if not any(t_row.values()):
            for key in t_row:
                t_row[key] += 1
        if not any(e_row.values()):
            for key in e_row:
                e_row[key] += 1
        ts, es = sum(t_row.values()), sum(e_row.values())
        for key in t_row:
            t_row[key] = round(t_row[key] / ts, 3)
        for key in e_row:
            e_row[key] = round(e_row[key] / es, 3)
    return transition, emission


def main():
    x = sys.stdin.readline().strip()
    sys.stdin.readline()
    alphabet = sys.stdin.readline().strip().split()
    sys.stdin.readline()
    path = sys.stdin.readline().strip()
    sys.stdin.readline()
    states = sys.stdin.readline().strip().split()
    transition, emission = parameters(x, alphabet, path, states)
    print('', *transition.keys(), sep='\t')
    for key in transition:
        print(key, *transition[key].values(), sep='\t')
    print('-' * 8)
    print('', *alphabet, sep='\t')
    for key in emission:
        print(key, *emission[key].values(), sep='\t')


if __name__ == '__main__':
    main()
