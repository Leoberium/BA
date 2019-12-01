import sys


def dbg(k, string):
    n = len(string)
    adj_dict = dict()
    for i in range(n - k + 1):
        k_mer = string[i:i+k]
        prefix = k_mer[:k-1]
        suffix = k_mer[1:]
        if prefix in adj_dict:
            adj_dict[prefix].append(suffix)
        else:
            adj_dict[prefix] = [suffix]
    return adj_dict


def main():
    k = int(sys.stdin.readline())
    text = sys.stdin.readline().strip()
    adj_list = dbg(k, string=text)
    for node in adj_list:
        print(node, '->', ','.join(adj_list[node]))


if __name__ == '__main__':
    main()
