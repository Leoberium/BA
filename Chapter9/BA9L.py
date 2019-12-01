import sys


class BWT:

    def __init__(self, transform):
        self.t = transform
        self.n = len(transform)
        self.last = list(transform)
        self.first = sorted(self.last)
        self.counts = {ch: [0] * self.n for ch in set(self.last)}
        self.compute_counts_array()
        self.lft = [-1] * self.n
        self.compute_last_to_first()

    def compute_counts_array(self):
        self.counts[self.last[0]][0] = 1
        for i in range(1, self.n):
            ch = self.last[i]
            for symbol in self.counts:
                if ch == symbol:
                    self.counts[symbol][i] = self.counts[symbol][i-1] + 1
                else:
                    self.counts[symbol][i] = self.counts[symbol][i-1]

    def compute_last_to_first(self):
        for i in range(self.n):
            ch = self.last[i]
            left, right = 0, self.n - 1

            while left < right:
                mid = (left + right) // 2
                if self.first[mid] < ch:
                    left = mid + 1
                else:
                    right = mid

            self.lft[i] = left + self.counts[ch][i] - 1

    def last_to_first(self, i):
        return self.lft[i]

    def invert_bwt(self):
        r, i = '$', 0
        while len(r) < self.n:
            r += self.first[self.lft[i]]
            i = self.lft[i]
        return r[::-1]

    def bw_matching(self, pattern):
        top, bottom = 0, self.n - 1
        while top <= bottom:
            if pattern:
                ch = pattern[-1]
                pattern = pattern[:-1]
                seg = self.t[top:bottom+1]
                if ch in seg:
                    top_index, bottom_index = top, bottom
                    for i in range(top, bottom + 1):
                        if self.t[i] == ch:
                            top_index = i
                            break
                    for i in range(bottom, top - 1, -1):
                        if self.t[i] == ch:
                            bottom_index = i
                            break
                    top = self.lft[top_index]
                    bottom = self.lft[bottom_index]
                else:
                    return 0
            else:
                return bottom - top + 1


def main():
    bwt = BWT(sys.stdin.readline().strip())
    a = []
    for pattern in sys.stdin.readline().strip().split():
        a.append(bwt.bw_matching(pattern))
    print(*a)


if __name__ == '__main__':
    main()
