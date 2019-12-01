import sys


class HMM:

    def __init__(self, a, s, t, e):
        self.a = a  # alphabet mapping to position in matrix
        self.index_to_ch = {i: ch for ch, i in self.a.items()}
        self.s = s  # states mapping to position in matrix
        self.index_to_state = {i: state for state, i in self.s.items()}
        self.t = t  # transition probabilities matrix
        self.e = e  # emission probabilities matrix

    def path_decoder(self, x):
        # outputs path: Viterbi algorithm
        path = ''
        n = len(x)

        # grid table and backtrack initialization
        grid = [[.0] * len(self.s) for _ in range(n)]
        backtrack = [[-1] * len(self.s) for _ in range(n)]

        # initial column
        ch = x[0]
        for i in range(len(self.s)):
            grid[0][i] = self.e[i][self.a[ch]]

        # filling the grid
        for j in range(1, n):
            ch = x[j]
            for i in range(len(self.s)):
                max_edge, max_index = -10 ** 6, -1
                for k in range(len(self.s)):
                    score = grid[j-1][k]
                    weight = self.t[k][i] * self.e[i][self.a[ch]]
                    edge = score * weight
                    if edge > max_edge:
                        max_edge = edge
                        max_index = k
                grid[j][i] = max_edge
                backtrack[j][i] = max_index

        # backtracking
        i = grid[-1].index(max(grid[-1]))
        path = self.index_to_state[i] + path
        for j in range(n - 1, 0, -1):
            i = backtrack[j][i]
            path = self.index_to_state[i] + path

        return path

    def decoding(self, x, path):
        n = len(x)
        nt = [[.0] * len(self.s) for _ in range(len(self.s))]
        et = [[.0] * len(self.a) for _ in range(len(self.s))]
        # first position
        ch, state = x[0], path[0]
        et[self.s[state]][self.a[ch]] += 1
        # counting
        for i in range(1, n):
            prev, cur = path[i-1], path[i]
            ch = x[i]
            nt[self.s[prev]][self.s[cur]] += 1
            et[self.s[cur]][self.a[ch]] += 1
        # normalization
        for i in range(len(self.s)):
            if not any(nt[i]):
                nt[i] = [1] * len(self.s)
            if not any(et[i]):
                et[i] = [1] * len(self.a)
            ns, es = sum(nt[i]), sum(et[i])
            for j in range(len(self.s)):
                nt[i][j] = nt[i][j] / ns
            for j in range(len(self.a)):
                et[i][j] = et[i][j] / es
        # reassigning
        self.t, self.e = nt, et

    def viterbi_learning(self, x, it):
        # iterations
        for _ in range(it):

            # updating path
            path = self.path_decoder(x)
            # updating emission and transition probabilities
            self.decoding(x, path)

    def output_transition_probabilities(self):
        print('', *list(self.s.keys()), sep='\t')
        for i in range(len(self.s)):
            row = [round(value, 3) for value in self.t[i]]
            print(self.index_to_state[i], *row, sep='\t')

    def output_emission_probabilities(self):
        print('', *list(self.a.keys()), sep='\t')
        for i in range(len(self.e)):
            row = [round(value, 3) for value in self.e[i]]
            print(self.index_to_state[i], *row, sep='\t')


def main():
    # reading x, path, alphabet and states
    it = int(sys.stdin.readline())
    sys.stdin.readline()
    x = sys.stdin.readline().strip()
    sys.stdin.readline()
    alphabet = {ch: i for i, ch in enumerate(sys.stdin.readline().strip().split())}
    sys.stdin.readline()
    states = {state: i for i, state in enumerate(sys.stdin.readline().strip().split())}
    sys.stdin.readline()
    sys.stdin.readline()
    # reading transition
    transition = []
    for _ in range(len(states)):
        transition.append(list(map(float, sys.stdin.readline().split()[1:])))
    sys.stdin.readline()
    sys.stdin.readline()
    # reading emission
    emission = []
    for _ in range(len(states)):
        emission.append(list(map(float, sys.stdin.readline().split()[1:])))
    # learning parameters
    model = HMM(a=alphabet, s=states, t=transition, e=emission)
    model.viterbi_learning(x=x, it=it)
    # outputting probabilities
    model.output_transition_probabilities()
    print('-' * 8)
    model.output_emission_probabilities()


if __name__ == '__main__':
    main()
