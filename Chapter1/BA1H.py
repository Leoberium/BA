import sys


def hamm_dist(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt


def approximate_occurrences_of_pattern(t, p, d):
    n, m = len(t), len(p)
    positions = []
    for i in range(n - m + 1):
        s = t[i:i+m]
        if hamm_dist(p, s) <= d:
            positions.append(i)
    return positions


def main():
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    d = int(sys.stdin.readline())
    print(len(approximate_occurrences_of_pattern(text, pattern, d)))


if __name__ == '__main__':
    main()
