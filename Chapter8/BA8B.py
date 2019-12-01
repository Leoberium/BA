import sys


def squared_distance(p1, p2):
    assert len(p1) == len(p2)
    d = 0.0
    for i in range(len(p1)):
        d += (p1[i] - p2[i])**2
    return d


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


def main():
    k, m = map(int, sys.stdin.readline().split())
    centers, data = [], []
    flag = False
    for line in sys.stdin:
        if line[0] == '-':
            flag = True
            continue
        row = list(map(float, line.split()))
        if flag:
            data.append(row)
        else:
            centers.append(row)
    assert len(centers) == k
    print(distortion(data, centers))



if __name__ == '__main__':
    main()
