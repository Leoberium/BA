import sys


symbol_to_number = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}


def pattern_to_number(p):
    if not p:
        return 0
    symbol = p[-1]
    prefix = p[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number[symbol]


def main():
    string = sys.stdin.readline().strip()
    print(pattern_to_number(string))


if __name__ == '__main__':
    main()
