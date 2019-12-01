import sys


def k_mer_comp(s, k):
    k_mers = set()
    for i in range(len(s) - k + 1):
        k_mers.add(s[i:i+k])
    return k_mers


def main():
    k = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    print(*k_mer_comp(s, k), sep='\n')


if __name__ == '__main__':
    main()
