import sys


def pattern_matching(s, p):
    n, m = len(s), len(p)
    positions = set()
    for i in range(n - m + 1):
        substring = s[i:i+m]
        if substring == p:
            positions.add(i)
    positions = [i for i in positions]
    positions.sort()
    return positions


def main():
    pattern = sys.stdin.readline().strip()
    string = sys.stdin.readline().strip()
    print(*pattern_matching(string, pattern))


if __name__ == '__main__':
    main()