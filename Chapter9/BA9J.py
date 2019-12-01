def inverse_bwt(t):
    last = list(t)
    first = sorted(last)
    # number of occurrences of each character up to current position
    occ = {ch: [0] * len(last) for ch in set(last)}
    occ[last[0]][0] = 1
    for j in range(1, len(last)):
        ch = last[j]
        for sym in occ:
            occ[sym][j] = occ[sym][j-1] + 1 if ch == sym else occ[sym][j-1]

    r, i = '$', 0
    while len(r) < len(t):

        ch = last[i]
        left, right = 0, len(last) - 1

        while left < right:
            m = (left + right) // 2
            if first[m] < ch:
                left = m + 1  # gives the index of the first occurrence of ch
            else:
                right = m

        left += occ[ch][i] - 1
        r += first[left]
        i = left

    return r[::-1]


def main():
    transform = input()
    print(inverse_bwt(transform))


if __name__ == '__main__':
    main()
