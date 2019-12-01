import sys


class HMM:

    def __init__(self, a, s, t, e, x):
        self.a = a  # alphabet mapping to position in matrix
        self.index_to_ch = {i: ch for ch, i in self.a.items()}
        self.s = s  # states mapping to position in matrix
        self.index_to_state = {i: state for state, i in self.s.items()}
        self.t = t  # transition probabilities matrix
        self.e = e  # emission probabilities matrix
        self.x = x  # string
        self.forward_grid = []
        self.backward_grid = []

    def update_string(self, x):
        self.x = x

    def update_grid(self):
        n = len(self.x)

        # forward grid
        self.forward_grid = [[.0] * len(self.s) for _ in range(n)]

        # initial column
        ch = self.x[0]
        for i in range(len(self.s)):
            self.forward_grid[0][i] = self.e[i][self.a[ch]]

        # filling the grid
        for j in range(1, n):
            ch = self.x[j]
            for i in range(len(self.s)):
                edge = 0
                for k in range(len(self.s)):
                    score = self.forward_grid[j-1][k]
                    weight = self.t[k][i] * self.e[i][self.a[ch]]
                    edge += score * weight
                self.forward_grid[j][i] = edge

        # the same for back grid
        self.backward_grid = [[.0] * len(self.s) for _ in range(n)]

        # last column
        for i in range(len(self.s)):
            # only transition
            self.backward_grid[-1][i] = 1

        # filling the grid
        for j in range(n - 2, -1, -1):
            ch = self.x[j+1]  # emission from the next column
            for i in range(len(self.s)):
                edge = 0
                for k in range(len(self.s)):
                    score = self.backward_grid[j+1][k]
                    weight = self.t[i][k] * self.e[k][self.a[ch]]
                    edge += score * weight
                self.backward_grid[j][i] = edge

    def forward(self, j, i):
        if not self.forward_grid:
            self.update_grid()
        return self.forward_grid[j][i]

    def forward_to_sink(self):
        if not self.forward_grid:
            self.update_grid()
        return sum(self.forward_grid[-1])

    def backward(self, j, i):
        if not self.backward_grid:
            self.update_grid()
        return self.backward_grid[j][i]

    def soft_decoding(self):
        self.update_grid()
        n = len(self.x)
        nt = [[.0] * len(self.s) for _ in range(len(self.s))]
        et = [[.0] * len(self.a) for _ in range(len(self.s))]

        # counting
        for j in range(n - 1):
            for i in range(len(self.s)):
                numerator = self.forward(j, i) * self.backward(j, i)
                et[i][self.a[self.x[j]]] += numerator / self.forward_to_sink()
                for k in range(len(self.s)):
                    weight = self.t[i][k] * self.e[k][self.a[self.x[j+1]]]
                    numerator = self.forward(j, i) * weight * self.backward(j + 1, k)
                    nt[i][k] += numerator / self.forward_to_sink()

        # last position
        for i in range(len(self.s)):
            numerator = self.forward(n - 1, i) * self.backward(n - 1, i)
            et[i][self.a[self.x[-1]]] += numerator / self.forward_to_sink()

        # normalization
        for i in range(len(self.s)):
            ns, es = sum(nt[i]), sum(et[i])
            for k in range(len(self.s)):
                nt[i][k] = nt[i][k] / ns
            for c in range(len(self.a)):
                et[i][c] = et[i][c] / es

        # reassigning
        self.t, self.e = nt, et

    def baum_welch_learning(self, it):
        # iterations
        for _ in range(it):
            self.update_grid()
            self.soft_decoding()

    def output_probabilities_along_path(self):
        self.update_grid()
        print(*list(self.s.keys()), sep='\t')
        for j in range(len(self.x)):
            row = []
            for i in range(len(self.s)):
                numerator = self.forward(j, i) * self.backward(j, i)
                row.append(round(numerator / self.forward_to_sink(), 4))
            print(*row, sep='\t')

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
    model = HMM(a=alphabet, s=states, t=transition, e=emission, x=x)
    model.baum_welch_learning(it)
    # outputting probabilities
    model.output_transition_probabilities()
    print('-' * 8)
    model.output_emission_probabilities()


if __name__ == '__main__':
    main()
