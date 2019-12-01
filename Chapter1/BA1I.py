import sys


number_to_symbol = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
}

symbol_to_number = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}


def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol[index]
    prefix_index = index // 4
    r = index % 4
    symbol = number_to_symbol[r]
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + symbol


def pattern_to_number(p):
    if not p:
        return 0
    symbol = p[-1]
    prefix = p[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number[symbol]


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


def freq_words(s, k, d):
    freq_pats = set()
    freq_dict = {}
    n = len(s)
    for i in range(n - k + 1):
        k_mer = s[i:i+k]
        neighborhood = neighbors(k_mer, d)
        for p in neighborhood:
            if p in freq_dict:
                freq_dict[p] += 1
            else:
                freq_dict[p] = 1
    max_count = max(freq_dict.values())
    for p, count in freq_dict.items():
        if count == max_count:
            freq_pats.add(p)
    return freq_pats


def main():
    text = sys.stdin.readline().strip()
    k, d = map(int, sys.stdin.readline().split())
    print(*freq_words(text, k, d))


if __name__ == '__main__':
    main()
