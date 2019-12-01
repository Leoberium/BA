import sys


def number_of_breakpoints(p):
    b = 0
    n = len(p)
    p.insert(0, 0)
    p.append(n + 1)
    for i in range(1, len(p)):
        if p[i] - p[i-1] != 1:
            b += 1
    return b


def main():
    sp = sys.stdin.readline().strip()
    sp = sp[1:(len(sp) - 1)]
    sp = list(map(int, sp.split()))
    print(number_of_breakpoints(sp))


if __name__ == '__main__':
    main()
