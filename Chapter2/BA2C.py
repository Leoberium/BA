import sys


def score(profile, k_mer):
    k = len(k_mer)
    prob = 1
    for i in range(k):
        ch = k_mer[i]
        if ch == 'A':
            prob *= profile[0][i]
        elif ch == 'C':
            prob *= profile[1][i]
        elif ch == 'G':
            prob *= profile[2][i]
        else:
            prob *= profile[3][i]
    return prob


def most_probable_k_mer(text, k, profile):
    n = len(text)
    scores = dict()
    for i in range(n - k + 1):
        k_mer = text[i:i+k]
        scores[k_mer] = score(profile, k_mer)
    max_score = max(scores.values())
    for k_mer, s in scores.items():
        if s == max_score:
            return k_mer


def main():
    text = sys.stdin.readline().strip()
    k = int(sys.stdin.readline())
    profile = []
    for i in range(4):
        row = list(map(float, sys.stdin.readline().split()))
        profile.append(row)
    print(most_probable_k_mer(text, k, profile))


if __name__ == '__main__':
    main()
