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


def main():
    string = sys.stdin.readline().strip()
    print(reverse_complement(string))


if __name__ == '__main__':
    main()