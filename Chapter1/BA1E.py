import sys


def clump_finding(genome, k, window_size, threshold):
    freq_pats = set()
    n = len(genome)
    freq_dict = dict()
    # initialization
    for i in range(window_size - k + 1):
        k_mer = genome[i:i+k]
        if k_mer in freq_dict:
            freq_dict[k_mer] += 1
        else:
            freq_dict[k_mer] = 1
    # searching for clumps
    for k_mer, freq in freq_dict.items():
        if freq >= threshold:
            freq_pats.add(k_mer)
    # sliding a window and searching
    right = window_size  # right position of window
    while right < n:
        left = right - window_size + 1  # left position of window
        rm_k_mer = genome[left-1:left-1+k]  # k-mer to remove
        freq_dict[rm_k_mer] -= 1
        add_k_mer = genome[right+1-k:right+1]  # k-mer to add
        if add_k_mer in freq_dict:
            freq_dict[add_k_mer] += 1
        else:
            freq_dict[add_k_mer] = 1
        if freq_dict[add_k_mer] >= threshold:
            freq_pats.add(add_k_mer)
        right += 1

    return freq_pats


def main():
    text = sys.stdin.readline().strip()
    k, length, t = map(int, sys.stdin.readline().split())
    print(len(clump_finding(genome=text, k=k, window_size=length, threshold=t)))


if __name__ == '__main__':
    main()
