import sys


def out_edges(state, nc):
    if len(state) == 1:
        if state == 'S':
            return ['I0', 'M1', 'D1']
        else:
            return []
    else:
        m, pos = state[0], state[1:]
        pos = int(pos)
        if pos == nc:
            if m == 'I':
                return [state, 'E']
            else:
                return ['I' + str(pos), 'E']
        else:
            if m == 'I':
                return [state, 'M' + str(pos + 1), 'D' + str(pos + 1)]
            else:
                return ['I' + str(pos), 'M' + str(pos + 1), 'D' + str(pos + 1)]


def in_edges(state, nc):
    if len(state) == 1:
        if state == 'E':
            return ['I' + str(nc), 'M' + str(nc), 'D' + str(nc)]
        else:
            return []
    else:
        m, pos = state[0], state[1:]
        pos = int(pos)
        if pos == 0:
            return ['S', state]
        if m == 'I':
            return [state, 'M' + str(pos), 'D' + str(pos)]
        else:
            if pos == 1:
                return ['S', 'I0']
            else:
                return ['I' + str(pos - 1), 'M' + str(pos - 1), 'D' + str(pos - 1)]


def profile_hmm(alphabet, alignment, t, pc):
    m, n = len(alignment[0]), len(alignment)
    alignment = [s[::-1] for s in alignment]

    # writing all transitions
    states = [['S'] for _ in range(n)]
    # writing all emissions
    counts = {}
    # current position
    pos = 0
    # all possible states
    st = ['S', 'I0']

    while any(alignment):
        column = [s.pop() for s in alignment]
        if column.count('-') / n > t:
            # insertion case
            ins = 'I' + str(pos)
            if ins not in counts:
                counts[ins] = {ch: 0 for ch in alphabet}
            for i in range(n):
                ch = column[i]
                if ch != '-':
                    states[i].append(ins)
                    counts[ins][ch] += 1
        else:
            pos += 1
            # match or deletion case
            match = 'M' + str(pos)
            deletion = 'D' + str(pos)
            ins = 'I' + str(pos)
            st += [match, deletion, ins]
            counts[match] = {ch: 0 for ch in alphabet}
            for i in range(n):
                ch = column[i]
                if ch != '-':
                    states[i].append(match)
                    counts[match][ch] += 1
                else:
                    states[i].append(deletion)

    # number of columns in seed alignment
    nc = pos

    for state in states:
        state.append('E')

    st.append('E')

    # transition probabilities
    transition = {state: {state: 0 for state in st} for state in st}
    for path in states:
        for i in range(1, len(path)):
            prev, cur = path[i-1], path[i]
            transition[prev][cur] += 1
    for key in transition:
        row = transition[key]
        c = sum(row.values())
        for state in row:
            row[state] = row[state] / c if row[state] > 0 else 0
    # accounting for pseudocounts
    for key in transition:
        row = transition[key]
        for state in out_edges(key, nc):
            row[state] += pc
        c = sum(row.values())
        for state in row:
            row[state] = round(row[state] / c, 3) if row[state] > 0 else 0

    # emission probabilities
    emission = {state: {ch: 0 for ch in alphabet} for state in st}
    for state in counts:
        p = counts[state]
        c = sum(p.values())
        for ch in p:
            emission[state][ch] += p[ch] / c if p[ch] > 0 else 0
    # accounting for pseudocounts
    for state in emission:
        if state[0] != 'I' and state[0] != 'M':
            continue
        p = emission[state]
        for ch in p:
            p[ch] += pc
        c = sum(p.values())
        for ch in p:
            p[ch] = round(p[ch] / c, 3)

    return transition, emission


def main():
    threshold, pc = map(float, sys.stdin.readline().strip().split())
    sys.stdin.readline()
    alphabet = sys.stdin.readline().strip().split()
    sys.stdin.readline()
    alignment = []
    for line in sys.stdin:
        line = line.strip()
        alignment.append(list(line))
    transition, emission = profile_hmm(alphabet, alignment, threshold, pc)
    print('', *transition.keys(), sep='\t')
    for key in transition:
        print(key, *transition[key].values(), sep='\t')
    print('-' * 8)
    print('', *alphabet, sep='\t')
    for key in emission:
        print(key, *emission[key].values(), sep='\t')


if __name__ == '__main__':
    main()
