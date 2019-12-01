import sys


def hd(s1, s2):
    assert len(s1) == len(s2)
    d = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            d += 1
    return d


def gkmt(text, k):
    # generates all k-mers from text
    km = []
    n = len(text)
    for i in range(n - k + 1):
        km.append(text[i:i+k])
    return km


def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    for string in dna:
        kms = gkmt(string, k)
        h_min = 2**16
        for k_mer in kms:
            h = hd(pattern, k_mer)
            if h < h_min:
                h_min = h
        distance += h_min
    return distance


def main():
    pattern = sys.stdin.readline().strip()
    dna = [s for s in sys.stdin.readline().strip().split()]
    print(distance_between_pattern_and_strings(pattern, dna))


if __name__ == '__main__':
    main()
