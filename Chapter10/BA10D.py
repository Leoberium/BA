import sys


def forward_to_sink(x, transition, emission):
    n = len(x)
    states = list(transition.keys())
    score = [{state: 0 for state in states} for i in range(n)]
    for state in states:
        score[0][state] = emission[state][x[0]] / len(states)

    for i in range(1, n):
        for state in states:
            layer = []
            for prev_state in states:
                weight = transition[prev_state][state] * emission[state][x[i]]
                t = weight * score[i-1][prev_state]
                layer.append(t)
            score[i][state] = sum(layer)

    sink = sum(score[n-1].values())

    return sink


def main():
    reader = (line.strip() for line in sys.stdin)
    x = next(reader)
    next(reader)
    alphabet = next(reader).split()
    next(reader)
    states = next(reader).split()
    next(reader)
    to = next(reader).split()
    transition = {}
    for state in states:
        p = enumerate(next(reader).split()[1:])
        transition[state] = {to[s]: float(prob) for s, prob in p}
    next(reader)
    emit = next(reader).split()
    emission = {}
    for state in states:
        p = enumerate(next(reader).split()[1:])
        emission[state] = {emit[s]: float(prob) for s, prob in p}
    # print(x)
    # print(alphabet)
    # print(states)
    # print(transition)
    # print(emission)
    print(forward_to_sink(x, transition, emission))


if __name__ == '__main__':
    main()
