import sys


def limb_length(d, leaf):
    n = len(d)
    limb = max(d[0])
    for j in range(n):
        if j == leaf:
            continue
        for k in range(j, n):
            if k == leaf:
                continue
            c = (d[leaf][j] + d[leaf][k] - d[j][k]) / 2
            if c < limb:
                limb = c
    return int(limb)


def linear_limb_length(d, leaf):
    # works if given leaf has at least one neighbor
    n = len(d)
    leaves = {_ for _ in range(n) if _ != leaf}
    while True:
        # choose some other leaf (must be not neighbor)
        k = leaves.pop()

        limb = max(d[0])
        for j in range(n):
            # cycle through all other leaves until we get to the neighbor of given leaf
            if j == k or j == leaf:
                continue
            c = (d[leaf][j] - (d[k][j] - d[k][leaf])) // 2
            if c < limb:
                limb = c

        # limb is zero if k is neighbor
        if limb != 0:
            break

    return limb


def main():
    n = int(sys.stdin.readline())
    j = int(sys.stdin.readline())
    assert 0 <= j <= n - 1
    d = []
    for _ in range(n):
        d.append(list(map(int, sys.stdin.readline().split())))
    assert len(d) == n
    print(linear_limb_length(d, j))


if __name__ == '__main__':
    main()
