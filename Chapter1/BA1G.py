import sys


def hamming_dist(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt


def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    print(hamming_dist(s1, s2))


if __name__ == '__main__':
    main()