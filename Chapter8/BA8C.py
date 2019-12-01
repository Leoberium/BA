import sys


def squared_distance(p1, p2):
    assert len(p1) == len(p2)
    m = len(p1)
    d = 0.0
    for i in range(m):
        d += (p1[i] - p2[i])**2
    return d**0.5


def distortion(data, centers):
    n = len(data)
    d = 0
    for data_point in data:
        min_sd = 10**10
        for center in centers:
            sd = squared_distance(data_point, center)
            if sd < min_sd:
                min_sd = sd
        d += min_sd
    return round(d / n, 3)


def lloyd_k_means(data, k):
    n = len(data)
    m = len(data[0])
    centers = [data[i] for i in range(k)]
    clusters = [[] for _ in range(k)]

    while True:

        # clustering data points
        for j in range(n):
            min_dist = 10**10
            cluster = -1
            for i in range(k):
                dist = squared_distance(centers[i], data[j])
                if dist < min_dist:
                    min_dist = dist
                    cluster = i

            clusters[cluster].append(j)

        # calculating new centers (of gravity)
        next_centers = [[0] * m for _ in range(k)]
        for i in range(k):
            size = len(clusters[i])
            for j in clusters[i]:
                for x in range(m):
                    next_centers[i][x] += data[j][x]
            for x in range(m):
                next_centers[i][x] = round(next_centers[i][x] / size, 3)

        if next_centers == centers:
            break
        else:
            centers = next_centers
            clusters = [[] for _ in range(k)]

    return centers


def main():
    k, m = map(int, sys.stdin.readline().split())
    data = []
    for line in sys.stdin:
        data.append(list(map(float, line.split())))
    for row in lloyd_k_means(data, k):
        print(*row)


if __name__ == '__main__':
    main()
