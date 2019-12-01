import sys


def hidden_path_probability(path, transition):
    prob = 1 / len(transition)
    for i in range(len(path) - 1):
        c = path[i]
        n = path[i+1]
        prob *= transition[c][n]
    return prob


def main():
    path = sys.stdin.readline().strip()
    sys.stdin.readline()
    states = sys.stdin.readline().split()
    sys.stdin.readline()
    cols = sys.stdin.readline().split()
    transition = {}
    for state in states:
        row = list(map(float, sys.stdin.readline().split()[1:]))
        t = []
        for i in range(len(cols)):
            t.append((cols[i], row[i]))
        transition[state] = {name: prob for name, prob in t}
    print(transition)
    print(hidden_path_probability(path, transition))


if __name__ == '__main__':
    main()
