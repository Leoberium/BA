def chromosome_to_cycle(chromosome):
    n = len(chromosome)
    nodes = [0] * 2 * n
    for j in range(n):
        i = chromosome[j]
        if i > 0:
            nodes[2 * j] = 2 * i - 1
            nodes[2 * j + 1] = 2 * i
        else:
            nodes[2 * j] = -2 * i
            nodes[2 * j + 1] = -2 * i - 1
    return nodes


def main():
    chromosome = input()
    chromosome = list(map(int, chromosome[1:len(chromosome)-1].split()))
    print('(' + ' '.join(map(str, chromosome_to_cycle(chromosome))) + ')')


if __name__ == '__main__':
    main()
