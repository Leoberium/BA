import sys


def string_reconstruction(patterns):
    k = len(patterns[0])
    n = len(patterns)
    string = patterns[0]
    for pattern in patterns[1:]:
        string += pattern[-1]
    return string


def paired_string_reconstruction(reads1, reads2, k, d):
    r1 = string_reconstruction(reads1)
    r2 = string_reconstruction(reads2)
    return r1 + r2[-(k+d):]


def main():
    k, d = map(int, sys.stdin.readline().split())
    reads1, reads2 = [], []
    for line in sys.stdin:
        read1, read2 = line.strip().split('|')
        reads1.append(read1)
        reads2.append(read2)
    print(paired_string_reconstruction(reads1, reads2, k, d))


if __name__ == '__main__':
    main()