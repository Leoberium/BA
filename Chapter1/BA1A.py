import sys


def pattern_count(text, pattern):
    cnt = 0
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            cnt += 1
    return cnt


def main():
    text = sys.stdin.readline().strip()
    pattern = sys.stdin.readline().strip()
    print(pattern_count(text, pattern))


if __name__ == '__main__':
    main()