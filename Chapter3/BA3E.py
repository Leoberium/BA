import sys


def dbg(patterns):
    k = len(patterns[0])
    adj_dict = dict()
    for pattern in patterns:
        prefix = pattern[:k-1]
        suffix = pattern[1:]
        if prefix in adj_dict:
            adj_dict[prefix].append(suffix)
        else:
            adj_dict[prefix] = [suffix]
    return adj_dict


def main():
    dna = []
    for line in sys.stdin:
        line = line.strip()
        dna.append(line)
    adj_list = dbg(dna)
    for node in adj_list:
        print(node, '->', ','.join(adj_list[node]))


if __name__ == '__main__':
    main()