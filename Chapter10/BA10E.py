import sys


def profile_hmm(alphabet, alignment, t):
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
            st += [match, deletion, 'I' + str(pos)]
            counts[match] = {ch: 0 for ch in alphabet}
            for i in range(n):
                ch = column[i]
                if ch != '-':
                    states[i].append(match)
                    counts[match][ch] += 1
                else:
                    states[i].append(deletion)

    for state in states:
        state.append('E')

    st.append('E')

    # transition probabilities
    transition = {state: {state: 0 for state in st} for state in st}
    for state in states:
        for i in range(1, len(state)):
            prev, cur = state[i-1], state[i]
            transition[prev][cur] += 1
    for key in transition:
        row = transition[key]
        c = sum(row.values())
        for state in row:
            row[state] = round(row[state] / c, 3) if row[state] > 0 else 0

    # emission probabilities
    emission = {state: {ch: 0 for ch in alphabet} for state in st}
    for state in counts:
        p = counts[state]
        c = sum(p.values())
        for ch in p:
            emission[state][ch] = round(p[ch] / c, 3) if p[ch] > 0 else 0
    return transition, emission


def main():
    threshold = float(sys.stdin.readline())
    sys.stdin.readline()
    alphabet = sys.stdin.readline().strip().split()
    sys.stdin.readline()
    alignment = []
    for line in sys.stdin:
        line = line.strip()
        alignment.append(list(line))
    transition, emission = profile_hmm(alphabet, alignment, threshold)
    print('', *transition.keys(), sep='\t')
    for key in transition:
        print(key, *transition[key].values(), sep='\t')
    print('-' * 8)
    print('', *alphabet, sep='\t')
    for key in emission:
        print(key, *emission[key].values(), sep='\t')


if __name__ == '__main__':
    main()
