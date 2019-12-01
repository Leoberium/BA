import sys


def tree_coloring(tree, colors):
    uncolored = {key for key in tree if key not in colors}
    while uncolored:
        # searching for ripe node
        for node in uncolored:
            children = tree[node]
            if all(map(lambda x: x in colors, children)):
                uncolored.remove(node)
                used_colors = {colors[child] for child in children}
                if len(used_colors) > 1:
                    colors[node] = 'purple'
                else:
                    colors[node] = used_colors.pop()
                break
    return colors


def main():
    flag = True
    tree = {}
    colors = {}
    for line in sys.stdin:
        line = line.strip()
        if line[0] == '-':
            flag = False
            continue
        if flag:
            u, a = line.split(' -> ')
            u = int(u)
            if a[0] == '{':
                tree[u] = []
            else:
                tree[u] = list(map(int, a.split(',')))
        else:
            u, c = line.split(': ')
            colors[int(u)] = c
    colors = tree_coloring(tree, colors)
    for key, value in colors.items():
        print(str(key) + ': ' + value)


if __name__ == '__main__':
    main()
