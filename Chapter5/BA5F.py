import sys


pam250 = {
    'A': {'A': 2, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N': 0, 'P': 1, 'Q': 0, 'R': -2, 'S': 1, 'T': 1, 'V': 0, 'W': -6, 'Y': -3},
    'C': {'A': -2, 'C': 12, 'D': -5, 'E': -5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S': 0, 'T': -2, 'V': -2, 'W': -8, 'Y': 0},
    'D': {'A': 0, 'C': -5, 'D': 4, 'E': 3, 'F': -6, 'G': 1, 'H': 1, 'I': -2, 'K': 0, 'L': -4, 'M': -3, 'N': 2, 'P': -1, 'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4},
    'E': {'A': 0, 'C': -5, 'D': 3, 'E': 4, 'F': -5, 'G': 0, 'H': 1, 'I': -2, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': -1, 'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4},
    'F': {'A': -3, 'C': -4, 'D': -6, 'E': -5, 'F': 9, 'G': -5, 'H': -2, 'I': 1, 'K': -5, 'L': 2, 'M': 0, 'N': -3, 'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W': 0, 'Y': 7},
    'G': {'A': 1, 'C': -3, 'D': 1, 'E': 0, 'F': -5, 'G': 5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N': 0, 'P': 0, 'Q': -1, 'R': -3, 'S': 1, 'T': 0, 'V': -1, 'W': -7, 'Y': -5},
    'H': {'A': -1, 'C': -3, 'D': 1, 'E': 1, 'F': -2, 'G': -2, 'H': 6, 'I': -2, 'K': 0, 'L': -2, 'M': -2, 'N': 2, 'P': 0, 'Q': 3, 'R': 2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y': 0},
    'I': {'A': -1, 'C': -2, 'D': -2, 'E': -2, 'F': 1, 'G': -3, 'H': -2, 'I': 5, 'K': -2, 'L': 2, 'M': 2, 'N': -2, 'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -5, 'Y': -1},
    'K': {'A': -1, 'C': -5, 'D': 0, 'E': 0, 'F': -5, 'G': -2, 'H': 0, 'I': -2, 'K': 5, 'L': -3, 'M': 0, 'N': 1, 'P': -1, 'Q': 1, 'R': 3, 'S': 0, 'T': 0, 'V': -2, 'W': -3, 'Y': -4},
    'L': {'A': -2, 'C': -6, 'D': -4, 'E': -3, 'F': 2, 'G': -4, 'H': -2, 'I': 2, 'K': -3, 'L': 6, 'M': 4, 'N': -3, 'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': 2, 'W': -2, 'Y': -1},
    'M': {'A': -1, 'C': -5, 'D': -3, 'E': -2, 'F': 0, 'G': -3, 'H': -2, 'I': 2, 'K': 0, 'L': 4, 'M': 6, 'N': -2, 'P': -2, 'Q': -1, 'R': 0, 'S': -2, 'T': -1, 'V': 2, 'W': -4, 'Y': -2},
    'N': {'A': 0, 'C': -4, 'D': 2, 'E': 1, 'F': -3, 'G': 0, 'H': 2, 'I': -2, 'K': 1, 'L': -3, 'M': -2, 'N': 2, 'P': 0, 'Q': 1, 'R': 0, 'S': 1, 'T': 0, 'V': -2, 'W': -4, 'Y': -2},
    'P': {'A': 1, 'C': -3, 'D': -1, 'E': -1, 'F': -5, 'G': 0, 'H': 0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N': 0, 'P': 6, 'Q': 0, 'R': 0, 'S': 1, 'T': 0, 'V': -1, 'W': -6, 'Y': -5},
    'Q': {'A': 0, 'C': -5, 'D': 2, 'E': 2, 'F': -5, 'G': -1, 'H': 3, 'I': -2, 'K': 1, 'L': -2, 'M': -1, 'N': 1, 'P': 0, 'Q': 4, 'R': 1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
    'R': {'A': -2, 'C': -4, 'D': -1, 'E': -1, 'F': -4, 'G': -3, 'H': 2, 'I': -2, 'K': 3, 'L': -3, 'M': 0, 'N': 0, 'P': 0, 'Q': 1, 'R': 6, 'S': 0, 'T': -1, 'V': -2, 'W': 2, 'Y': -4},
    'S': {'A': 1, 'C': 0, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': 1, 'Q': -1, 'R': 0, 'S': 2, 'T': 1, 'V': -1, 'W': -2, 'Y': -3},
    'T': {'A': 1, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 0, 'H': -1, 'I': 0, 'K': 0, 'L': -2, 'M': -1, 'N': 0, 'P': 0, 'Q': -1, 'R': -1, 'S': 1, 'T': 3, 'V': 0, 'W': -5, 'Y': -3},
    'V': {'A': 0, 'C': -2, 'D': -2, 'E': -2, 'F': -1, 'G': -1, 'H': -2, 'I': 4, 'K': -2, 'L': 2, 'M': 2, 'N': -2, 'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -6, 'Y': -2},
    'W': {'A': -6, 'C': -8, 'D': -7, 'E': -7, 'F': 0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4, 'P': -6, 'Q': -5, 'R': 2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y': 0},
    'Y': {'A': -3, 'C': 0, 'D': -4, 'E': -4, 'F': 7, 'G': -5, 'H': 0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2, 'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W': 0, 'Y': 10}
}


def score_matrix_reader():
    names = sys.stdin.readline().split()
    m = {aa: {} for aa in names}
    for i in range(len(m)):
        row = sys.stdin.readline().split()
        for j, aa in enumerate(names):
            m[row[0]].update({aa: int(row[j + 1])})
    return m


def alignment_table(s1, s2, score, sigma):
    ni, nj = len(s1), len(s2)
    d = [[0] * (nj + 1) for _ in range(ni + 1)]
    pi, pj, max_score = 0, 0, 0
    for i in range(1, ni + 1):
        for j in range(1, nj + 1):
            delta = score[s1[i-1]][s2[j-1]]
            d[i][j] = max([
                d[i-1][j] - sigma,
                d[i][j-1] - sigma,
                d[i-1][j-1] + delta,
                0
            ])
            if d[i][j] > max_score:
                max_score = d[i][j]
                # pointers
                pi, pj = i, j
    return d, pi, pj


def local_alignment(s1, s2, score, sigma):
    d, i, j = alignment_table(s1, s2, score=score, sigma=sigma)
    a = [d[i][j]]
    r1 = ''
    r2 = ''
    while i > 0 and j > 0:
        delta = score[s1[i - 1]][s2[j - 1]]
        if d[i - 1][j - 1] + delta == d[i][j] and i > 0 and j > 0:
            r1 += s1[i - 1]
            r2 += s2[j - 1]
            i -= 1
            j -= 1
        elif d[i - 1][j] - sigma == d[i][j] and i > 0:
            r1 += s1[i - 1]
            r2 += '-'
            i -= 1
        elif d[i][j - 1] - sigma == d[i][j] and j > 0:
            r1 += '-'
            r2 += s2[j - 1]
            j -= 1
        else:
            break
    a.append(r1[::-1])
    a.append(r2[::-1])
    return a


def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    a = local_alignment(s1, s2, score=pam250, sigma=5)
    for o in a:
        print(o)


if __name__ == '__main__':
    main()