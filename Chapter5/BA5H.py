import sys


def fitting_alignment(s1, s2):
    n, m = len(s1), len(s2)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    # local for s1, global for s2
    for j in range(1, m + 1):
        d[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            q = 1 if s1[i-1] == s2[j-1] else -1
            d[i][j] = max(
                d[i-1][j] - 1,
                d[i][j-1] - 1,
                d[i-1][j-1] + q
            )
    # searching for the best score
    index = 0
    s = d[0][m]
    for i in range(1, n):
        if d[i][m] > s:
            s = d[i][m]
            index = i
    i, j = index, m
    r1, r2 = '', ''
    # backtracking
    while j > 0 and i > 0:
        if d[i][j] == d[i - 1][j - 1] + 1 and s1[i - 1] == s2[j - 1]:
            r1 += s1[i - 1]
            r2 += s2[j - 1]
            i -= 1
            j -= 1
        elif d[i][j] == d[i][j - 1] - 1:
            r1 += '-'
            r2 += s2[j - 1]
            j -= 1
        elif d[i][j] == d[i - 1][j - 1] - 1:
            r1 += s1[i - 1]
            r2 += s2[j - 1]
            i -= 1
            j -= 1
        elif d[i][j] == d[i - 1][j] - 1:
            r1 += s1[i - 1]
            r2 += '-'
            i -= 1
    return d[index][m], r1[::-1], r2[::-1]


def main():
    v = sys.stdin.readline().strip()
    w = sys.stdin.readline().strip()
    for o in fitting_alignment(v, w):
        print(o)


if __name__ == '__main__':
    main()
