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

    highest_score = -1
    for house_r in range(max_r):
        for house_c in range(max_c):
            score = 1
            current = forest[house_r][house_c]

            # right
            trees = 0
            for c in range(house_c+1, max_c):
                trees += 1
                if forest[house_r][c] >= current:
                    break
            score *= trees

            # left
            trees = 0
            for c in range(house_c-1, -1, -1):
                trees += 1
                if forest[house_r][c] >= current:
                    break
            score *= trees

            # up
            trees = 0
            for r in range(house_r-1, -1, -1):
                trees += 1
                if forest[r][house_c] >= current:
                    break
            score *= trees

            # down
            trees = 0
            for r in range(house_r+1, max_r):
                trees += 1
                if forest[r][house_c] >= current:
                    break
            score *= trees

            if score > highest_score:
                highest_score = score

    print(highest_score)
