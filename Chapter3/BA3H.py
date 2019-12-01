import sys


def string_reconstruction(patterns):
    k = len(patterns[0])
    n = len(patterns)
    prefixes = [pattern[:k-1] for pattern in patterns]
    suffixes = [pattern[1:] for pattern in patterns]
    string = ''
    start = 0
    for i in range(n):
        prefix = prefixes[i]
        if prefix not in suffixes:
            string += patterns[i]
            start = i
            break
    unused = {i for i in range(n) if i != start}
    while unused:
        suffix = string[-(k-1):]
        for i in unused:
            prefix = prefixes[i]
            if suffix == prefix:
                string += suffixes[i][-1]
                unused.remove(i)
                break
    return string


def main():
    k = int(sys.stdin.readline())
    patterns = []
    for line in sys.stdin:
        line = line.strip()
        assert len(line) == k
        patterns.append(line)
    print(string_reconstruction(patterns))


if __name__ == '__main__':
    main()
