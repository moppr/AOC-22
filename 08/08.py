with open("08.in") as f:
    forest = [[int(tree) for tree in line.strip()] for line in f]
    visible = set()
    max_r = len(forest)
    max_c = len(forest[0])

    for r in range(max_r):
        # left to right
        highest = -1
        for c in range(max_c):
            if forest[r][c] > highest:
                visible.add((r, c))
                highest = forest[r][c]
        # right to left
        highest = -1
        for c in range(max_c-1, -1, -1):
            if forest[r][c] > highest:
                visible.add((r, c))
                highest = forest[r][c]
    for c in range(max_c):
        # top to bottom
        highest = -1
        for r in range(max_r):
            if forest[r][c] > highest:
                visible.add((r, c))
                highest = forest[r][c]
        # bottom to top
        highest = -1
        for r in range(max_r-1, -1, -1):
            if forest[r][c] > highest:
                visible.add((r, c))
                highest = forest[r][c]
    print(len(visible))
