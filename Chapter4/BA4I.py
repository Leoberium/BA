import sys


def convolution_spectrum(spectrum):
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
    for m, freq in f.items():
        c.append((freq, m))
    c.sort()
    conv_spectrum = []
    while c:
        freq, m = c.pop()
        conv_spectrum += [m for _ in range(freq)]
    return conv_spectrum


def alphabet(spectrum, m):
    a = []
    n = len(spectrum)
    i = 0
    while m > 0 and i < n:
        aa_mass = spectrum[i]
        if aa_mass not in a and 57 <= aa_mass <= 200:
            a.append(aa_mass)
            m -= 1
        i += 1
    return a


def mass(peptide):
    m = sum(map(int, peptide.split('-')))
    return m


def expand(ps, masses):
    for peptide in ps.copy():
        ps.remove(peptide)
        for m in masses:
            if peptide:
                new_peptide = peptide + '-' + str(m)
            else:
                new_peptide = str(m)
            ps.add(new_peptide)
    return ps


def linear_spectrum(peptide):
    cs = [0]
    if not peptide:
        return cs
    composition = list(map(int, peptide.split('-')))
    n = len(composition)
    for k in range(1, n):
        for i in range(n - k + 1):
            cs.append(sum(composition[i:i+k]))
    cs.append(mass(peptide))
    cs.sort()
    return cs


def cyclic_spectrum(peptide):
    cs = [0]
    if not peptide:
        return cs
    composition = list(map(int, peptide.split('-')))
    n = len(composition)
    for k in range(1, n):
        for i in range(n):
            if i + k <= n:
                cs.append(sum(composition[i:i+k]))
            else:
                r = i + k - n
                cs.append(sum(composition[i:] + composition[:r]))
    cs.append(mass(peptide))
    cs.sort()
    return cs


def score(peptide, spectrum, cyclic=True):
    if cyclic:
        peptide_spectrum = cyclic_spectrum(peptide)
    else:
        peptide_spectrum = linear_spectrum(peptide)
    p_dict, s_dict = dict(), dict()
    for value in peptide_spectrum:
        if value in p_dict:
            p_dict[value] += 1
        else:
            p_dict[value] = 1
    for value in spectrum:
        if value in s_dict:
            s_dict[value] += 1
        else:
            s_dict[value] = 1
    s = 0
    for value in p_dict:
        if value in s_dict:
            s += min(p_dict[value], s_dict[value])
    return s


def trim(leader_board, spectrum, n):
    scores = []
    for peptide in leader_board:
        s = score(peptide, spectrum, cyclic=True)
        scores.append((s, peptide))
    scores.sort(reverse=True)
    for j in range(n, len(scores)):
        if scores[j][0] < scores[n-1][0]:
            scores = scores[:j]
            break
    leader_board = set()
    for s, peptide in scores:
        leader_board.add(peptide)
    return leader_board


def convolution_cyclopeptide_sequencing(spectrum, n, m):
    leader_board = {''}
    leader_peptide = ''
    parent_mass = max(spectrum)
    conv_spectrum = convolution_spectrum(spectrum)
    masses = alphabet(conv_spectrum, m)
    while leader_board:
        leader_board = expand(leader_board, masses)
        for peptide in leader_board.copy():
            if mass(peptide) == parent_mass:
                if score(peptide, spectrum) > \
                        score(leader_peptide, spectrum):
                    leader_peptide = peptide
            elif mass(peptide) > parent_mass:
                leader_board.remove(peptide)
        leader_board = trim(leader_board, spectrum, n)
    return leader_peptide


def main():
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    spectrum = list(map(int, sys.stdin.readline().split()))
    print(convolution_cyclopeptide_sequencing(spectrum, n, m))
    # c = convolution_spectrum([0, 97, 99, 114, 128, 147, 147, 163,
    #                           186, 227, 241, 242, 244, 260, 261, 262,
    #                           283, 291, 333, 340, 357, 385, 389, 390,
    #                           390, 405, 430, 430, 447, 485, 487, 503,
    #                           504, 518, 543, 544, 552, 575, 577, 584,
    #                           632, 650, 651, 671, 672, 690, 691, 738,
    #                           745, 747, 770, 778, 779, 804, 818, 819,
    #                           820, 835, 837, 875, 892, 917, 932, 932,
    #                           933, 934, 965, 982, 989, 1030, 1039, 1060,
    #                           1061, 1062, 1078, 1080, 1081, 1095, 1136, 1159,
    #                           1175, 1175, 1194, 1194, 1208, 1209, 1223, 1225,
    #                           1322])
    # print(c)
    # print(alphabet(c, 10))


if __name__ == '__main__':
    main()
