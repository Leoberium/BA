import sys


def min_skew(s):
    positions = []
    skew = [0]
    for ch in s:
        if ch == 'C':
            skew.append(skew[-1] - 1)
        elif ch == 'G':
            skew.append(skew[-1] + 1)
        else:
            skew.append(skew[-1])
    min_skew_value = min(skew)
    for i in range(len(skew)):
        if skew[i] == min_skew_value:
            positions.append(i)
    return positions


def main():
    text = sys.stdin.readline().strip()
    print(*min_skew(text))


if __name__ == '__main__':
    main()
