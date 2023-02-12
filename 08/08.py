with open("08.in") as f:
    forest = [[int(tree) for tree in line.strip()] for line in f]
    visible = set()

    for r in range(len(forest)):
        # left to right
        highest = -1
        for c in range(len(forest[r])):
            if forest[r][c] > highest:
                visible.add((r, c))
                highest = forest[r][c]
        # right to left
        highest = -1
        for c in range(len(forest[r])-1, -1, -1):
            if forest[r][c] > highest:
                visible.add((r, c))
                highest = forest[r][c]
    for c in range(len(forest[0])):
        # top to bottom
        highest = -1
        for r in range(len(forest)):
            if forest[r][c] > highest:
                visible.add((r, c))
                highest = forest[r][c]
        # bottom to top
        highest = -1
        for r in range(len(forest)-1, -1, -1):
            if forest[r][c] > highest:
                visible.add((r, c))
                highest = forest[r][c]
    print(len(visible))
