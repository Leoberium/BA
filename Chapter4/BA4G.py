import sys


masses = [
    57, 71, 87, 97, 99,
    101, 103, 113, 114, 115,
    128, 129, 131, 137, 147,
    156, 163, 186
]


def mass(peptide):
    m = sum(map(int, peptide.split('-')))
    return m


def expand(ps):
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


# linear score to trim the leaderboard
def linear_score(peptide, spectrum):
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


# cyclic score for the leader peptide
def cyclic_score(peptide, spectrum):
    peptide_spectrum = cyclic_spectrum(peptide)
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
        score = linear_score(peptide, spectrum)
        scores.append((score, peptide))
    scores.sort(reverse=True)
    for j in range(n, len(scores)):
        if scores[j][0] < scores[n-1][0]:
            scores = scores[:j]
            break
    leader_board = set()
    for score, peptide in scores:
        leader_board.add(peptide)
    return leader_board


def leaderboard_cyclopeptide_sequencing(spectrum, n):
    leader_board = {''}
    leader_peptide = ''
    parent_mass = max(spectrum)
    while leader_board:
        leader_board = expand(leader_board)
        for peptide in leader_board.copy():
            if mass(peptide) == parent_mass:
                if cyclic_score(peptide, spectrum) > \
                        cyclic_score(leader_peptide, spectrum):
                    leader_peptide = peptide
            elif mass(peptide) > parent_mass:
                leader_board.remove(peptide)
        leader_board = trim(leader_board, spectrum, n)
    return leader_peptide


def main():
    n = int(sys.stdin.readline())
    spectrum = list(map(int, sys.stdin.readline().split()))
    print(leaderboard_cyclopeptide_sequencing(spectrum, n))


if __name__ == '__main__':
    main()
