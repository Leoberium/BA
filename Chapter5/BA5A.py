import sys


def min_number(money, coins):
    arr = [0] * (money + 1)
    for m in range(1, money + 1):
        min_n = money
        for c in coins:
            r = m - c
            if r < 0:
                continue
            if arr[r] < min_n:
                min_n = arr[r]
        arr[m] = min_n + 1
    return arr[money]


def main():
    money = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split(',')))
    print(min_number(money, coins))


if __name__ == '__main__':
    main()
