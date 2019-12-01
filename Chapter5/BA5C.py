import sys


def table(s1, s2):
    ni, nj = len(s1), len(s2)
    d = [[0] * (nj + 1) for i in range(ni + 1)]
    for i in range(1, ni + 1):
        for j in range(1, nj + 1):
            if s1[i-1] == s2[j-1]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])
    return d


def lcs(s1, s2):
    d = table(s1, s2)
    rev_string = ''
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            i -= 1
            j -= 1
            rev_string += s1[i]
            continue
        if d[i][j] == d[i-1][j]:
            i -= 1
        if d[i][j] == d[i][j-1]:
            j -= 1
    return rev_string[::-1]


def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    print(*table(s1, s2), sep='\n')
    print(lcs(s1, s2))


if __name__ == '__main__':
    main()
