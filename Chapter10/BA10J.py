import sys


def backward(x, transition, emission, step, st='source'):
    n = len(x)
    states = transition.keys()
    if step > n or step < -1:
        raise IndexError
    if step >= n - 1 or st == 'sink':
        return 1

    score = [{state: 0 for state in states} for i in range(step + 1, n)]
    if step == -1 or st == 'source':
        for state in states:
            score[0][states] = emission[state][x[0]] / len(states)
    else:
        for state in states:
            score[0][state] = transition[st][state] * emission[state][x[step+1]]

    for i in range(step + 2, n):
        index = i - step - 1
        for state in states:
            layer = []
            for prev_state in states:
                weight = transition[prev_state][state] * emission[state][x[i]]
                t = weight * score[index-1][prev_state]
                layer.append(t)
            score[index][state] = sum(layer)

    return sum(score[-1].values())


def forward(x, transition, emission, step, st='sink'):
    n = len(x)
    states = transition.keys()
    if step > n or step < -1:
        raise IndexError
    if step == -1 or st == 'source':
        return 1
    if step == 0:
        return emission[st][x[0]] / len(states)

    score = [{state: 0 for state in states} for i in range(step)]
    for state in states:
        score[0][state] = emission[state][x[0]] / len(states)

    for i in range(1, step):
        for state in states:
            layer = []
            for prev_state in states:
                weight = transition[prev_state][state] * emission[state][x[i]]
                t = weight * score[i - 1][prev_state]
                layer.append(t)
            score[i][state] = sum(layer)

    if step < n:
        t = 0
        for prev_state in states:
            weight = transition[prev_state][st] * emission[st][x[step]]
            t += weight * score[step-1][prev_state]
        return t
    else:
        return sum(score[-1].values())


def soft_decoder(x, transition, emission):
    n = len(x)
    states = list(transition.keys())
    p = {state: [0] * len(x) for state in states}
    for pos in range(n):
        for state in states:
            f = forward(x, transition, emission, step=pos, st=state)
            s = forward(x, transition, emission, step=n)
            b = backward(x, transition, emission, step=pos, st=state)
            print(f, b)
            p[state][pos] = round(f * b / s, 4)
    return p


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
    print(x)
    print(alphabet)
    print(states)
    print(transition)
    print(emission)

    probabilities = soft_decoder(x, transition, emission)
    print(*list(probabilities.keys()))
    for pos in range(len(x)):
        print(*[probabilities[state][pos] for state in probabilities.keys()])


if __name__ == '__main__':
    main()
