import sys


def overlap_alignment(s1, s2):
    n, m = len(s1), len(s2)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    # local alignment
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            q = 1 if s1[i-1] == s2[j-1] else -2
            d[i][j] = max(
                d[i-1][j] - 2,
                d[i][j-1] - 2,
                d[i-1][j-1] + q
            )
    # searching for the best prefix score
    index = 0
    s = d[0][m]
    for j in range(m, 0, -1):
        if d[n][j] > s:
            s = d[n][j]
            index = j
    i, j = n, index
    r1, r2 = '', ''
    # backtracking
    while j > 0 and i > 0:
        if d[i][j] == d[i - 1][j - 1] + 1 and s1[i - 1] == s2[j - 1]:
            r1 += s1[i - 1]
            r2 += s2[j - 1]
            i -= 1
            j -= 1
        elif d[i][j] == d[i][j - 1] - 2:
            r1 += '-'
            r2 += s2[j - 1]
            j -= 1
        elif d[i][j] == d[i - 1][j - 1] - 2:
            r1 += s1[i - 1]
            r2 += s2[j - 1]
            i -= 1
            j -= 1
        elif d[i][j] == d[i - 1][j] - 2:
            r1 += s1[i - 1]
            r2 += '-'
            i -= 1
    return d[n][index], r1[::-1], r2[::-1]


def main():
    v = sys.stdin.readline().strip()
    w = sys.stdin.readline().strip()
    for o in overlap_alignment(v, w):
        print(o)


if __name__ == '__main__':
    main()
