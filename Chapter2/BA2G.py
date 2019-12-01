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


def generate_k_mer_from_profile(profile, string):
    k = len(profile[0])
    k_mers = generate_k_mers(string, k)
    n = len(k_mers)
    probs = list(map(prob_score, [profile] * n, k_mers))
    c = sum(probs)
    norm_probs = [prob / c for prob in probs]
    motif = random.choices(k_mers, weights=norm_probs, k=1)
    return motif.pop()  # because it is a list


def gibbs_sampler(dna, k, t, n):
    dna_k_mers = map(generate_k_mers, dna, [k] * len(dna))
    motifs = [random.choice(k_mers) for k_mers in dna_k_mers]
    best_motifs = motifs
    for j in range(n):
        index = random.choice(range(t))
        motifs_subset = [motifs[i] for i in range(t) if i != index]
        profile = profile_former(motifs_subset)
        motifs[index] = generate_k_mer_from_profile(profile, dna[index])
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


def rep_gs(dna, k, t, n, niter):
    best_motifs = []
    best_score = 2**16
    for j in range(niter):
        motifs = gibbs_sampler(dna, k, t, n)
        cur_score = score(motifs)
        if cur_score < best_score:
            best_motifs = motifs
            best_score = cur_score
    return best_motifs


def main():
    k, t, n = map(int, sys.stdin.readline().split())
    dna = []
    for i in range(t):
        dna.append(sys.stdin.readline().strip())
    assert len(dna) == t
    motifs = rep_gs(dna, k, t, n, niter=20)
    for motif in motifs:
        print(motif)


if __name__ == '__main__':
    main()
