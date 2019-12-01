import sys
from math import exp


def distance(p1, p2):
    assert len(p1) == len(p2)
    m = len(p1)
    d = 0.0
    for i in range(m):
        d += (p1[i] - p2[i])**2
    return d**0.5


def soft_k_means(data, k, b):
    n = len(data)
    m = len(data[0])
    centers = [data[i] for i in range(k)]
    while True:

        # computing hidden matrix
        hidden_matrix = [[0.0] * n for _ in range(k)]
        for j in range(n):
            denominator = 0
            for i in range(k):
                denominator += exp(-b * distance(data[j], centers[i]))
            for i in range(k):
                numerator = exp(-b * distance(data[j], centers[i]))
                hidden_matrix[i][j] = numerator / denominator

        # computing new centers
        prev_centers = centers
        centers = [[0.0] * m for _ in range(k)]
        for i in range(k):
            denominator = sum(hidden_matrix[i])
            for x in range(m):
                numerator = 0
                for j in range(n):
                    numerator += hidden_matrix[i][j] * data[j][x]
                centers[i][x] = round(numerator / denominator, 3)

        if prev_centers == centers:
            break

    return centers


def main():
    k, m = map(int, sys.stdin.readline().split())
    beta = float(sys.stdin.readline())
    data = []
    for line in sys.stdin:
        data.append(list(map(float, line.split())))
    for row in soft_k_means(data, k, beta):
        print(*row)


if __name__ == '__main__':
    main()
