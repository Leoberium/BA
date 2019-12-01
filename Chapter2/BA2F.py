import sys
import random


def score(motifs):
    t = len(motifs)
    k = len(motifs[0])
    s = 0
    for i in range(k):
        col = [motif[i] for motif in motifs]
        ch_freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for ch in col:
            ch_freq[ch] += 1
        max_freq = max(ch_freq.values())
        s += t - max_freq
    return s


def generate_k_mers(text, k):
    n = len(text)
    k_mers = []
    for i in range(n - k + 1):
        k_mer = text[i:i+k]
        k_mers.append(k_mer)
    return k_mers


def profile_former(motifs):
    t = len(motifs)
    k = len(motifs[0])
    profile = [[.0] * k for _ in range(4)]
    for j in range(k):
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


def motifs_finder(profile, dna):
    found_motifs = []
    k = len(profile[0])
    for string in dna:
        k_mers = generate_k_mers(string, k)
        max_prob = 0
        best_k_mer = k_mers[0]
        for k_mer in k_mers:
            prob = prob_score(profile, k_mer)
            if prob > max_prob:
                max_prob = prob
                best_k_mer = k_mer
        found_motifs.append(best_k_mer)
    return found_motifs


def randomized_motif_search(dna, k):
    dna_k_mers = map(generate_k_mers, dna, [k] * len(dna))
    # motifs = [random.choice(k_mers) for k_mers in dna_k_mers]
    motifs = ['CCA', 'CCT', 'CTT', 'TTG']
    best_motifs = motifs
    while True:
        profile = profile_former(motifs)
        motifs = motifs_finder(profile, dna)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


def run_rns(dna, k, niter):
    best_score = 2**16
    best_motifs = []
    for i in range(niter):
        motifs = randomized_motif_search(dna, k)
        cur_score = score(motifs)
        if cur_score < best_score:
            best_motifs = motifs
            best_score = cur_score
    return best_motifs


def main():
    k, t = map(int, sys.stdin.readline().split())
    dna = []
    for i in range(t):
        dna.append(sys.stdin.readline().strip())
    assert len(dna) == t
    motifs = run_rns(dna, k, 1000)
    for motif in motifs:
        print(motif)


if __name__ == '__main__':
    main()
