import sys


def convolution(spectrum):
    n = len(spectrum)
    f = dict()
    for i in range(n):
        for j in range(n):
            diff = spectrum[i] - spectrum[j]
            if diff <= 0:
                continue
            if diff in f:
                f[diff] += 1
            else:
                f[diff] = 1
    c = []
    for mass, freq in f.items():
        c.append((freq, mass))
    c.sort(reverse=True)
    conv = []
    for freq, mass in c:
        conv += [mass for _ in range(freq)]
    conv.sort()
    return conv


def main():
    spectrum = list(map(int , sys.stdin.readline().split()))
    print(*convolution(spectrum))


if __name__ == '__main__':
    main()
