import sys
from random import randint


def distance(p1, p2):
    assert len(p1) == len(p2)
    d = 0.0
    for i in range(len(p1)):
        d += (p1[i] - p2[i])**2
    return d**0.5


def farthest_first_traversal(data, k):
    n = len(data)
    # centers = [data[randint(0, n - 1)]]
    # the first point from data according to the task formulation
    centers = [data[0]]
    while len(centers) < k:
        max_d, max_data_point = 0, 0
        for i in range(n):
            data_point = data[i]
            min_d = 10**10
            for center in centers:
                d = distance(center, data_point)
                if d < min_d:
                    min_d = d
            if min_d > max_d:
                max_d = min_d
                max_data_point = data_point

        centers.append(max_data_point)

    return centers


def main():
    k, m = map(int, sys.stdin.readline().split())
    data = []
    for line in sys.stdin:
        data.append(list(map(float, line.split())))
    for center in farthest_first_traversal(data, k):
        print(*center)


if __name__ == '__main__':
    main()
