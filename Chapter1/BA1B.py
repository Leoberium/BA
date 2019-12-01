import sys


def most_frequent_k_mers(text, k):

    freq_pats = set()
    freq_dict = dict()

    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i+k]
        if pattern in freq_dict:
            freq_dict[pattern] += 1
        else:
            freq_dict[pattern] = 1

    max_count = max(freq_dict.values())
    for pattern, count in freq_dict.items():
        if count == max_count:
            freq_pats.add(pattern)

    return freq_pats


def main():
    text = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())
    print(*most_frequent_k_mers(text, k))


if __name__ == '__main__':
    main()
