import sys


def edit_distance(s1, s2):
    ni, nj = len(s1), len(s2)
    d = [[0] * (nj + 1) for i in range(ni + 1)]
    for i in range(1, ni + 1):
        d[i][0] = i
    for j in range(1, nj + 1):
        d[0][j] = j
    for i in range(1, ni + 1):
        for j in range(1, nj + 1):
            diff = 0 if s1[i-1] == s2[j-1] else 1
            d[i][j] = min([
                d[i-1][j] + 1,
                d[i][j-1] + 1,
                d[i-1][j-1] + diff
            ])
    return d[ni][nj]


def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    print(edit_distance(s1, s2))


if __name__ == '__main__':
    main()
