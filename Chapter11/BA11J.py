import sys


aa_to_mass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
    'T': 101, 'C': 103, 'L': 113, 'I': 113, 'N': 114,
    'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186,
    'X': 4, 'Z': 5
}

mass_to_aa = {
    57: ['G'], 71: ['A'], 87: ['S'], 97: ['P'],
    99: ['V'], 101: ['T'], 103: ['C'], 113: ['L', 'I'],
    114: ['N'], 115: ['D'], 128: ['K', 'Q'], 129: ['E'],
    131: ['M'], 137: ['H'], 147: ['F'], 156: ['R'],
    163: ['Y'], 186: ['W'], 4: ['X'], 5: ['Z']
}


def spectral_alignment(spectrum, peptide, k):
    md = len(spectrum)  # mass + delta
    spectrum.insert(0, 0)

    # computing prefix masses
    pm = [0]
    mass = 0
    for aa in peptide:
        mass += aa_to_mass[aa]
        pm.append(mass)
    n = len(pm)  # number of prefixes

    #    spectral alignment graph
    sag = [{m: [0] * (md + 1) for m in pm} for _ in range(k + 1)]
    for t in range(1, k + 1):
        sag[t][0][0] = -10**6

    # backtrack points to previous layer and previous j
    backtrack = [{m: [(-1, -1)] * (md + 1) for m in pm} for _ in range(k + 1)]

    # filling zero modifications layer
    for i in range(1, n):
        prev, cur = pm[i-1], pm[i]
        if cur > md:
            break
        sag[0][cur][cur] = spectrum[cur] + sag[0][prev][prev]
        backtrack[0][cur][cur] = (0, prev)

    # filling all other layers
    for t in range(1, k + 1):
        for i in range(t, n):
            prev, cur = pm[i-1], pm[i]
            diff = cur - prev
            prev_score = []
            for j in range(md + 1):
                prev_score.append(sag[t-1][prev][j])
            for j in range(1, md + 1):
                # non-diagonal score
                nd_score = max(prev_score[:j])
                which = prev_score[:j].index(nd_score)
                # diagonal score
                d_score = -10**6
                if j >= diff:
                    d_score = sag[t][prev][j-diff]
                if d_score > nd_score:
                    sag[t][cur][j] = spectrum[j] + d_score
                    backtrack[t][cur][j] = (t, j-diff)
                else:
                    sag[t][cur][j] = spectrum[j] + nd_score
                    backtrack[t][cur][j] = (t-1, which)

    # modified peptide
    mp = ''

    # backtracking
    t, i, j = k, n - 1, md
    while i > 0:
        new_t, new_j = backtrack[t][pm[i]][j]
        aa = peptide[i-1]
        if new_t == t:
            mp = aa + mp
        else:
            aa_mass = pm[i] - pm[i-1]
            emp_mass = j - new_j
            diff = emp_mass - aa_mass
            mp = aa + '(' + ('-', '+')[diff > 0] + str(abs(diff)) + ')' + mp
        i -= 1
        t, j = new_t, new_j

    return mp


def main():
    peptide = sys.stdin.readline().strip()
    spectrum = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    print(spectral_alignment(spectrum, peptide, k))


if __name__ == '__main__':
    main()