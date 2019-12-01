import sys


def multiple_alignment(s1, s2, s3):
    n, m, p = len(s1), len(s2), len(s3)
    d = [[[0] * (p + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    b = [[[0] * (p + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        b[i][0][0] = 0
    for j in range(1, m + 1):
        b[0][j][0] = 1
    for k in range(1, p + 1):
        b[0][0][k] = 2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, p + 1):
                score = [
                    d[i-1][j][k],
                    d[i][j-1][k],
                    d[i][j][k-1],
                    d[i-1][j-1][k],
                    d[i-1][j][k-1],
                    d[i][j-1][k-1],
                    d[i-1][j-1][k-1] + (s1[i-1] == s2[j-1] == s3[k-1])
                ]
                d[i][j][k] = max(score)
                b[i][j][k] = score.index(d[i][j][k])
    i, j, k = n, m, p
    r1, r2, r3 = '', '', ''
    while i > 0 or j > 0 or k > 0:
        if i > 0 and b[i][j][k] == 0:
            r1 += s1[i-1]
            r2 += '-'
            r3 += '-'
            i -= 1
        elif j > 0 and b[i][j][k] == 1:
            r1 += '-'
            r2 += s2[j-1]
            r3 += '-'
            j -=1
        elif k > 0 and b[i][j][k] == 2:
            r1 += '-'
            r2 += '-'
            r3 += s3[k-1]
            k -= 1
        elif i > 0 and j > 0 and b[i][j][k] == 3:
            r1 += s1[i-1]
            r2 += s2[j-1]
            r3 += '-'
            i -= 1
            j -= 1
        elif i > 0 and k > 0 and b[i][j][k] == 4:
            r1 += s1[i-1]
            r2 += '-'
            r3 += s3[k-1]
            i -= 1
            k -= 1
        elif j > 0 and k > 0 and b[i][j][k] == 5:
            r1 += '-'
            r2 += s2[j-1]
            r3 += s3[k-1]
            j -= 1
            k -= 1
        else:
            r1 += s1[i-1]
            r2 += s2[j-1]
            r3 += s3[k-1]
            i -= 1
            j -= 1
            k -= 1
    return d[n][m][p], r1[::-1], r2[::-1], r3[::-1]


def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    s3 = sys.stdin.readline().strip()
    for o in multiple_alignment(s1, s2, s3):
        print(o)


if __name__ == '__main__':
    main()
