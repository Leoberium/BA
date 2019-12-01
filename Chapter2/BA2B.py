import sys


def hamming_dist(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt


def min_hamming_dist(pattern, text):
    n = len(text)
    k = len(pattern)
    distances = []
    for i in range(n - k + 1):
        sub_text = text[i:i+k]
        d = hamming_dist(sub_text, pattern)
        distances.append(d)
    return min(distances)


def median_string(dna, k):
    d = dict()
    for s in dna:
        n = len(s)
        for i in range(n - k + 1):
            pattern = s[i:i+k]
            d[pattern] = 0
            for dna_i in dna:
                d[pattern] += min_hamming_dist(pattern, dna_i)
    d_min = min(d.values())
    for p, value in d.items():
        if value == d_min:
            return p


def main():
    k = int(sys.stdin.readline())
    dna = []
    for line in sys.stdin:
        line = line.strip()
        dna.append(line)
    print(median_string(dna, k))


if __name__ == '__main__':
    main()
