import sys
sys.setrecursionlimit(10**6)


def turnpike_reconstruct(dist):
    n = len(dist)  # number of distances
    m = int(n**0.5)  # number of points
    allowed = [True] * n  # which distances can be used
    solution = [0]

    def solve(m):
        # if we have accumulated solution
        if len(solution) == m:
            return True

        # current max distance
        j = len(dist) - 1
        while not allowed[j]:
            j -= 1
        max_d = dist[j]

        for point in solution:
            new_point = abs(max_d - point)  # new candidate solution
            if new_point in solution:
                continue
            # generate distances with new point
            new_dist = set()
            for x in solution:
                new_dist.add(x - new_point)
                new_dist.add(new_point - x)
            # testing if its distance with all other is present
            indices = set()  # indices to disallow
            for j in range(len(dist)):
                if not allowed[j]:
                    continue
                if dist[j] in new_dist:
                    new_dist.remove(dist[j])
                    indices.add(j)
            if new_dist:  # if any of distances with new point left
                continue
            # disallowing corresponding distances
            for i in indices:
                allowed[i] = False
            solution.append(new_point)
            # trying to solve with this new set
            s = solve(m)
            if s:
                return True
            else:
                solution.pop()
                for i in indices:
                    allowed[i] = True

        return False

    solve(m)

    solution.sort()

    return solution


def main():
    delta_a = list(map(int, sys.stdin.readline().split()))
    print(*turnpike_reconstruct(delta_a))


if __name__ == '__main__':
    main()
