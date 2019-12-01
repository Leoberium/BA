import sys


def hamming_dist(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt


def neighbors(pattern, d):
    nucleotides = {'A', 'C', 'G', 'T'}
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return nucleotides
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for p in suffix_neighbors:
        if hamming_dist(pattern[1:], p) < d:
            for x in nucleotides:
                neighborhood.add(x + p)
        else:
            neighborhood.add(pattern[0] + p)
    return neighborhood


def motif_enumeration(dna, k, d):
    patterns = set()
    for s in dna:
        n = len(s)
        for i in range(n - k + 1):
            pattern = s[i:i+k]
            neighborhood = neighbors(pattern, d)
            for pattern_prime in neighborhood:
                appears = [False] * len(dna)
                for a in range(len(dna)):
                    dna_str = dna[a]
                    m = len(dna_str)
                    for j in range(m - k + 1):
                        sub_str = dna_str[j:j+k]
                        if hamming_dist(sub_str, pattern_prime) <= d:
                            appears[a] = True
                            break
                if all(appears):
                    patterns.add(pattern_prime)
    return patterns


def main():
    k, d = map(int, sys.stdin.readline().split())
    str_col = []
    for line in sys.stdin:
        line = line.strip()
        str_col.append(line)
    print(*motif_enumeration(str_col, k, d))


if __name__ == '__main__':
    main()
