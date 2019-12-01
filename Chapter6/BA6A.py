import sys


def greedy_sorting(p):
    permutations = []
    for i in range(len(p)):
        if abs(p[i]) != i + 1:

            index = 0

            for j in range(i + 1, len(p)):
                if abs(p[j]) == i + 1:
                    index = j
                    break

            m = (index - i) // 2

            for j in range(m + 1):
                p[j + i], p[index - j] = -p[index - j], -p[j + i]

            permutations.append(p.copy())

            if p[i] == -(i + 1):
                p[i] = -p[i]
                permutations.append(p.copy())

        if p[i] == -(i + 1):
            p[i] = -p[i]
            permutations.append(p.copy())

    return permutations


def main():
    sp = sys.stdin.readline().strip()
    sp = sp[1:(len(sp) - 1)]
    sp = list(map(int, sp.split()))
    for p in greedy_sorting(sp):
        p = list(map(lambda x: '+' + str(x) if x > 0 else str(x), p))
        print('(', ' '.join(p), ')', sep='')


if __name__ == '__main__':
    main()
