import sys


def reverse_complement(s):
    r = ''
    rev_dict = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    for ch in s:
        r += rev_dict[ch]
    return r[::-1]


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
    max_count = 1
    for p in freq_dict:
        count = freq_dict[p]
        p_r = reverse_complement(p)
        if p_r in freq_dict:
            count += freq_dict[p_r]
        if count > max_count:
            max_count = count
    for p, count in freq_dict.items():
        p_r = reverse_complement(p)
        if p_r in freq_dict:
            count += freq_dict[p_r]
        if count == max_count:
            freq_pats.add(p)
    return freq_pats


def main():
    text = sys.stdin.readline().strip()
    k, d = map(int, sys.stdin.readline().split())
    print(*freq_words(text, k, d))


if __name__ == '__main__':
    main()