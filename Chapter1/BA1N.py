import sys


nucleotides = {'A', 'C', 'G', 'T'}


def d_neighborhood(pattern, d):
    neighborhood = {pattern}
    for i in range(d):
        for pat in neighborhood.copy():
            for j in range(len(pat)):
                for nucleotide in nucleotides:
                    s = pat[:j] + nucleotide + pat[j+1:]
                    neighborhood.add(s)
    return neighborhood


def main():
    pattern = sys.stdin.readline().strip()
    d = int(sys.stdin.readline())
    print(len(d_neighborhood(pattern, d)), sep='\n')


if __name__ == '__main__':
    main()
