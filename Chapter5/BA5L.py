import sys


blosum62 = {
    'A': {'A': 4, 'C': 0, 'D': -2, 'E': -1, 'F': -2, 'G': 0, 'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': -2, 'P': -1, 'Q': -1, 'R': -1, 'S': 1, 'T': 0, 'V': 0, 'W': -3, 'Y': -2},
    'C': {'A': 0, 'C': 9, 'D': -3, 'E': -4, 'F': -2, 'G': -3, 'H': -3, 'I': -1, 'K': -3, 'L': -1, 'M': -1, 'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -1, 'T': -1, 'V': -1, 'W': -2, 'Y': -2},
    'D': {'A': -2, 'C': -3, 'D': 6, 'E': 2, 'F': -3, 'G': -1, 'H': -1, 'I': -3, 'K': -1, 'L': -4, 'M': -3, 'N': 1, 'P': -1, 'Q': 0, 'R': -2, 'S': 0, 'T': -1, 'V': -3, 'W': -4, 'Y': -3},
    'E': {'A': -1, 'C': -4, 'D': 2, 'E': 5, 'F': -3, 'G': -2, 'H': 0, 'I': -3, 'K': 1, 'L': -3, 'M': -2, 'N': 0, 'P': -1, 'Q': 2, 'R': 0, 'S': 0, 'T': -1, 'V': -2, 'W': -3, 'Y': -2},
    'F': {'A': -2, 'C': -2, 'D': -3, 'E': -3, 'F': 6, 'G': -3, 'H': -1, 'I': 0, 'K': -3, 'L': 0, 'M': 0, 'N': -3, 'P': -4, 'Q': -3, 'R': -3, 'S': -2, 'T': -2, 'V': -1, 'W': 1, 'Y': 3},
    'G': {'A': 0, 'C': -3, 'D': -1, 'E': -2, 'F': -3, 'G': 6, 'H': -2, 'I': -4, 'K': -2, 'L': -4, 'M': -3, 'N': 0, 'P': -2, 'Q': -2, 'R': -2, 'S': 0, 'T': -2, 'V': -3, 'W': -2, 'Y': -3},
    'H': {'A': -2, 'C': -3, 'D': -1, 'E': 0, 'F': -1, 'G': -2, 'H': 8, 'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': 1, 'P': -2, 'Q': 0, 'R': 0, 'S': -1, 'T': -2, 'V': -3, 'W': -2, 'Y': 2},
    'I': {'A': -1, 'C': -1, 'D': -3, 'E': -3, 'F': 0, 'G': -4, 'H': -3, 'I': 4, 'K': -3, 'L': 2, 'M': 1, 'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -2, 'T': -1, 'V': 3, 'W': -3, 'Y': -1},
    'K': {'A': -1, 'C': -3, 'D': -1, 'E': 1, 'F': -3, 'G': -2, 'H': -1, 'I': -3, 'K': 5, 'L': -2, 'M': -1, 'N': 0, 'P': -1, 'Q': 1, 'R': 2, 'S': 0, 'T': -1, 'V': -2, 'W': -3, 'Y': -2},
    'L': {'A': -1, 'C': -1, 'D': -4, 'E': -3, 'F': 0, 'G': -4, 'H': -3, 'I': 2, 'K': -2, 'L': 4, 'M': 2, 'N': -3, 'P': -3, 'Q': -2, 'R': -2, 'S': -2, 'T': -1, 'V': 1, 'W': -2, 'Y': -1},
    'M': {'A': -1, 'C': -1, 'D': -3, 'E': -2, 'F': 0, 'G': -3, 'H': -2, 'I': 1, 'K': -1, 'L': 2, 'M': 5, 'N': -2, 'P': -2, 'Q': 0, 'R': -1, 'S': -1, 'T': -1, 'V': 1, 'W': -1, 'Y': -1},
    'N': {'A': -2, 'C': -3, 'D': 1, 'E': 0, 'F': -3, 'G': 0, 'H': 1, 'I': -3, 'K': 0, 'L': -3, 'M': -2, 'N': 6, 'P': -2, 'Q': 0, 'R': 0, 'S': 1, 'T': 0, 'V': -3, 'W': -4, 'Y': -2},
    'P': {'A': -1, 'C': -3, 'D': -1, 'E': -1, 'F': -4, 'G': -2, 'H': -2, 'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': -2, 'P': 7, 'Q': -1, 'R': -2, 'S': -1, 'T': -1, 'V': -2, 'W': -4, 'Y': -3},
    'Q': {'A': -1, 'C': -3, 'D': 0, 'E': 2, 'F': -3, 'G': -2, 'H': 0, 'I': -3, 'K': 1, 'L': -2, 'M': 0, 'N': 0, 'P': -1, 'Q': 5, 'R': 1, 'S': 0, 'T': -1, 'V': -2, 'W': -2, 'Y': -1},
    'R': {'A': -1, 'C': -3, 'D': -2, 'E': 0, 'F': -3, 'G': -2, 'H': 0, 'I': -3, 'K': 2, 'L': -2, 'M': -1, 'N': 0, 'P': -2, 'Q': 1, 'R': 5, 'S': -1, 'T': -1, 'V': -3, 'W': -3, 'Y': -2},
    'S': {'A': 1, 'C': -1, 'D': 0, 'E': 0, 'F': -2, 'G': 0, 'H': -1, 'I': -2, 'K': 0, 'L': -2, 'M': -1, 'N': 1, 'P': -1, 'Q': 0, 'R': -1, 'S': 4, 'T': 1, 'V': -2, 'W': -3, 'Y': -2},
    'T': {'A': 0, 'C': -1, 'D': -1, 'E': -1, 'F': -2, 'G': -2, 'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': 0, 'P': -1, 'Q': -1, 'R': -1, 'S': 1, 'T': 5, 'V': 0, 'W': -2, 'Y': -2},
    'V': {'A': 0, 'C': -1, 'D': -3, 'E': -2, 'F': -1, 'G': -3, 'H': -3, 'I': 3, 'K': -2, 'L': 1, 'M': 1, 'N': -3, 'P': -2, 'Q': -2, 'R': -3, 'S': -2, 'T': 0, 'V': 4, 'W': -3, 'Y': -1},
    'W': {'A': -3, 'C': -2, 'D': -4, 'E': -3, 'F': 1, 'G': -2, 'H': -2, 'I': -3, 'K': -3, 'L': -2, 'M': -1, 'N': -4, 'P': -4, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': -3, 'W': 11, 'Y': 2},
    'Y': {'A': -2, 'C': -2, 'D': -3, 'E': -2, 'F': 3, 'G': -3, 'H': 2, 'I': -1, 'K': -2, 'L': -1, 'M': -1, 'N': -2, 'P': -3, 'Q': -1, 'R': -2, 'S': -2, 'T': -2, 'V': -1, 'W': 2, 'Y': 7}
}


# def alignment_table(s1, s2):
#     ni, nj = len(s1), len(s2)
#     d = [[0] * (nj + 1) for _ in range(ni + 1)]
#     for i in range(1, ni + 1):
#         d[i][0] = - i * 5
#     for j in range(1, nj + 1):
#         d[0][j] = - j * 5
#     for i in range(1, ni + 1):
#         for j in range(1, nj + 1):
#             delta = blosum62[s1[i-1]][s2[j-1]]
#             d[i][j] = max([
#                 d[i-1][j] - 5,
#                 d[i][j-1] - 5,
#                 d[i-1][j-1] + delta
#             ])
#     return d
#
#
# def global_alignment(s1, s2):
#     d = alignment_table(s1, s2)
#     i, j = len(s1), len(s2)
#     r1 = ''
#     r2 = ''
#     while i > 0 or j > 0:
#         delta = blosum62[s1[i-1]][s2[j-1]]
#         if d[i-1][j-1] + delta == d[i][j] and i > 0 and j > 0:
#             r1 += s1[i-1]
#             r2 += s2[j-1]
#             i -= 1
#             j -= 1
#             continue
#         if d[i-1][j] - 5 == d[i][j] and i > 0:
#             r1 += s1[i-1]
#             r2 += '-'
#             i -= 1
#             continue
#         if d[i][j-1] - 5 == d[i][j] and j > 0:
#             r1 += '-'
#             r2 += s2[j-1]
#             j -= 1
#             continue
#     return r1[::-1], r2[::-1]


def middle_edge(si, sj):
    n, m = len(si), len(sj)
    node, edge_type = 0, 0
    column = len(sj) // 2
    # from source
    cur = [-5 * i for i in range(n + 1)]
    for j in range(1, column + 1):
        prev = cur
        cur = [0] * (n + 1)
        cur[0] = -5 * j
        node = 0
        for i in range(1, n + 1):
            edges = [
                prev[i] - 5,
                prev[i - 1] + blosum62[si[i - 1]][sj[j - 1]],
                cur[i - 1] - 5
            ]
            cur[i] = max(edges)
    fs = cur
    si, sj = si[::-1], sj[::-1]
    # to sink
    cur = [-5 * i for i in range(n + 1)]
    prev = cur
    for j in range(1, m - column + 1):
        prev = cur
        cur = [0] * (n + 1)
        cur[0] = -5 * j
        for i in range(1, n + 1):
            edges = [
                prev[i] - 5,
                prev[i - 1] + blosum62[si[i - 1]][sj[j - 1]],
                cur[i - 1] - 5
            ]
            cur[i] = max(edges)

    ts = cur
    max_length, node = -10**10, 0
    for i in range(n + 1):
        if fs[i] + ts[n-i] > max_length:
            node = i
            max_length = fs[i] + ts[n-i]
    # 0 - horizontal, 1 - diagonal, 2 - vertical
    edges = [
        prev[n-node] - 5,
        prev[n-node-1] + blosum62[si[n-node-1]][sj[m-column-1]],
        cur[n-node-1] - 5
    ]
    edge_type = edges.index(ts[n-node])
    return node, edge_type


def linear_space_alignment(top, bottom, left, right, si, sj):
    if left == right:
        return si[top:bottom], '-' * (bottom - top)
    if top == bottom:
        return '-' * (right - left), sj[left:right]
    # if bottom - top == 1 or right - left == 1:
    #     return global_alignment(si[top:bottom], sj[left:right])
    middle = (left + right) // 2
    mid_node, mid_edge = middle_edge(si[top:bottom], sj[left:right])
    mid_node += top
    i1, j1 = linear_space_alignment(top, mid_node, left, middle, si, sj)
    if mid_edge == 0:
        i0, j0 = '-', sj[middle]
        middle += 1
    elif mid_edge == 1:
        i0, j0 = si[mid_node], sj[middle]
        middle += 1
        mid_node += 1
    else:
        i0, j0 = si[mid_node], '-'
        mid_node += 1
    i2, j2 = linear_space_alignment(mid_node, bottom, middle, right, si, sj)
    return i1 + i0 + i2, j1 + j0 + j2


def lsa(si, sj):
    n, m = len(si), len(sj)
    a1, a2 = linear_space_alignment(0, n, 0, m, si, sj)
    s = 0
    for i in range(len(a1)):
        ch1, ch2 = a1[i], a2[i]
        if '-' in (ch1, ch2):
            s -= 5
        else:
            s += blosum62[ch1][ch2]
    return s, a1, a2


def main():
    v = sys.stdin.readline().strip()
    w = sys.stdin.readline().strip()
    for o in lsa(v, w):
        print(o)


if __name__ == '__main__':
    main()
