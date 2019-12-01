import sys


number_to_symbol = {
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
}


def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol[index]
    prefix_index = index // 4
    r = index % 4
    symbol = number_to_symbol[r]
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + symbol


def main():
    index = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    print(number_to_pattern(index, k))


if __name__ == '__main__':
    main()
