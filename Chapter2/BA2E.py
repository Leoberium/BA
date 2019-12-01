import sys


def score(motifs):
    t = len(motifs)
    n = len(motifs[0])
    s = 0
    for i in range(n):
        col = [motif[i] for motif in motifs]
        ch_freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for ch in col:
            ch_freq[ch] += 1
        max_freq = max(ch_freq.values())
        s += t - max_freq
    return s


def generate_all_k(text, k):
    n = len(text)
    k_mers = []
    for i in range(n - k + 1):
        k_mers.append(text[i:i+k])
    return k_mers


def prob_score(profile, k_mer):
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


def profile_former(motifs):
    t = len(motifs)
    n = len(motifs[0])
    profile = [[.0] * n for _ in range(4)]
    for j in range(n):
        col = [0] * 4
        for i in range(t):
            ch = motifs[i][j]
            if ch == 'A':
                col[0] += 1
            elif ch == 'C':
                col[1] += 1
            elif ch == 'G':
                col[2] += 1
            else:
                col[3] += 1
        for i in range(4):
            profile[i][j] = (col[i] + 1) / (t + 4)
    return profile


def greedy_motif_search(dna, k, t):
    best_motifs = [s[:k] for s in dna]
    n = len(dna[0])
    for i in range(n - k + 1):
        motif = dna[0][i:i+k]
        motifs = [motif]
        for j in range(1, t):
            profile = profile_former(motifs)
            max_prob_score = 0
            max_k_mer = dna[j][:k]
            k_mers = generate_all_k(dna[j], k)
            for k_mer in k_mers:
                k_mer_score = prob_score(profile, k_mer)
                if k_mer_score > max_prob_score:
                    max_prob_score = k_mer_score
                    max_k_mer = k_mer
            motifs.append(max_k_mer)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


def main():
    k, t = map(int, sys.stdin.readline().split())
    dna = []
    for i in range(t):
        dna.append(sys.stdin.readline().strip())
    motifs = greedy_motif_search(dna, k, t)
    for motif in motifs:
        print(motif)


if __name__ == '__main__':
    main()
