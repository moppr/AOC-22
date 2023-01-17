with open("02.in") as f:
    score = 0
    sc1 = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
    sc2 = {0: 3, 1: 6, 2: 0}

    for line in f:
        p1, p2 = line.split()
        score += sc1[p2]
        score += sc2[(sc1[p2] - sc1[p1]) % 3]

    print(score)
