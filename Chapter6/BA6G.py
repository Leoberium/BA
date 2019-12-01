def cycle_to_chromosome(nodes):
    n = len(nodes)
    chromosome = []
    for i in range(0, n, 2):
        p1, p2 = nodes[i], nodes[i+1]
        if p1 < p2:
            chromosome.append('+' + str(p2 // 2))
        else:
            chromosome.append('-' + str(p1 // 2))
    return chromosome


def main():
    nodes = input()
    nodes = list(map(int, nodes[1:len(nodes)-1].split()))
    print('(' + ' '.join(cycle_to_chromosome(nodes)) + ')')


if __name__ == '__main__':
    main()