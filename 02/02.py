with open("02.in") as f:
    score1, score2 = 0, 0
    sc1 = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
    sc2 = {0: 3, 1: 6, 2: 0, 'X': 0, 'Y': 3, 'Z': 6}
    sc3 = {'X': 2, 'Y': 0, 'Z': 1}

    for line in f:
        p1, p2 = line.split()
        score1 += sc1[p2]
        score1 += sc2[(sc1[p2] - sc1[p1]) % 3]
        score2 += (sc1[p1] + sc3[p2] - 1) % 3 + 1
        score2 += sc2[p2]

    print(score1, score2)
