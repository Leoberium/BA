import re


def rev_comp(s):
    r = ''
    d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    for ch in s:
        r += d[ch]
    return r[::-1]


def shared_k_mers(k, s1, s2):
    k_mers = []
    for i in range(len(s1) - k + 1):
        k_mer = s1[i:i+k]
        rc_k_mer = rev_comp(k_mer)
        for x in re.finditer(k_mer, s2):
            k_mers.append((i, x.start()))
        for x in re.finditer(rc_k_mer, s2):
            k_mers.append((i, x.start()))
    return k_mers


def main():
    k = int(input())
    v = input()
    w = input()
    for k_mer in shared_k_mers(k, v, w):
        print(k_mer)


if __name__ == '__main__':
    main()
