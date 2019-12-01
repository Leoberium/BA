import sys


def outcome_probability(path, x, emission):
    prob = 1
    for i in range(len(path)):
        prob *= emission[path[i]][x[i]]
    return prob


def main():
    x = sys.stdin.readline().strip()
    sys.stdin.readline()
    alphabet = sys.stdin.readline().split()
    sys.stdin.readline()
    path = sys.stdin.readline().strip()
    sys.stdin.readline()
    states = sys.stdin.readline().split()
    sys.stdin.readline()
    emission = {}
    chars = sys.stdin.readline().split()
    for state in states:
        probabilities = list(map(float, sys.stdin.readline().split()[1:]))
        t = []
        for i in range(len(chars)):
            t.append((chars[i], probabilities[i]))
        emission[state] = {char: prob for char, prob in t}
    print(outcome_probability(path, x, emission))


if __name__ == '__main__':
    main()
