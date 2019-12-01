def bwt(s):
    n = len(s)
    # cyclic rotations
    cr = []
    for i in range(n):
        cr.append(s[i:] + s[:i])
    cr.sort()
    return ''.join([x[-1] for x in cr])


def main():
    text = input()
    print(bwt(text))


if __name__ == '__main__':
    main()
