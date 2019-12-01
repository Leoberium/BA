import sys


aa_to_mass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
    'T': 101, 'C': 103, 'L': 113, 'I': 113, 'N': 114,
    'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
    'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186,
    'X': 4, 'Z': 5
}

mass_to_aa = {
    57: ['G'], 71: ['A'], 87: ['S'], 97: ['P'],
    99: ['V'], 101: ['T'], 103: ['C'], 113: ['L', 'I'],
    114: ['N'], 115: ['D'], 128: ['K', 'Q'], 129: ['E'],
    131: ['M'], 137: ['H'], 147: ['F'], 156: ['R'],
    163: ['Y'], 186: ['W'], 4: ['X'], 5: ['Z']
}


def vector_to_peptide(p):
    n = len(p)
    cnt = 0
    peptide = ''
    for i in range(n):
        cnt += 1
        if p[i] == 1:
            peptide += mass_to_aa[cnt][0]
            cnt = 0
    return peptide


def main():
    p = list(map(int, sys.stdin.readline().split()))
    print(vector_to_peptide(p))


if __name__ == '__main__':
    main()
