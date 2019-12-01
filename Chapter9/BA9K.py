def last_to_first(t, i):
    last = list(t)
    first = sorted(last)
    # number of occurrences of each character up to current position
    occ = {ch: [0] * len(last) for ch in set(last)}
    occ[last[0]][0] = 1
    for j in range(1, len(last)):
        ch = last[j]
        for sym in occ:
            occ[sym][j] = occ[sym][j-1] + 1 if ch == sym else occ[sym][j-1]
    left, right = 0, len(last) - 1
    ch = last[i]
    while left < right:
        m = (left + right) // 2
        if first[m] < ch:
            left = m + 1  # gives the index of the first occurrence of ch
        else:
            right = m
    return left + occ[ch][i] - 1


def main():
    transform = input()
    i = int(input())
    print(last_to_first(transform, i))


if __name__ == '__main__':
    main()
