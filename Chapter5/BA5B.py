import sys


def manhattan_tourist(n, m, down, right):
    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        s[i][0] = s[i-1][0] + down[i-1][0]
    for j in range(1, m + 1):
        s[0][j] = s[0][j-1] + right[0][j-1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i-1][j] + down[i-1][j],
                          s[i][j-1] + right[i][j-1])
    return s[n][m]


def main():
    n, m = map(int, sys.stdin.readline().split())
    down, right = [], []
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        assert len(row) == m + 1
        down.append(row)
    sys.stdin.readline()
    for i in range(n + 1):
        row = list(map(int, sys.stdin.readline().split()))
        assert len(row) == m
        right.append(row)
    print(manhattan_tourist(n, m, down, right))


if __name__ == '__main__':
    main()
