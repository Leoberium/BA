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


def computing_frequencies(text, k):
    frequency_array = [0] * 4**k
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    return frequency_array


def main():
    text = sys.stdin.readline().strip()
    k = int(sys.stdin.readline())
    print(*computing_frequencies(text, k))


if __name__ == '__main__':
    main()
