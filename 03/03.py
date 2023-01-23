def prio(x):
    return ord(x) - 64 + 26 if x.isupper() else ord(x) - 96


with open("03.in") as f:

    prio1 = prio2 = 0
    for i, sack in enumerate(f):
        sack = sack.strip()
        half = len(sack)//2
        c1, c2 = sack[:half], sack[half:]

        for item in set(c1):
            if item in c2:
                prio1 += prio(item)
                break

        if i % 3 == 0:
            g1 = sack
        elif i % 3 == 1:
            g2 = sack
        else:
            g3 = sack
            for item in set(g1):
                if item in g2 and item in g3:
                    prio2 += prio(item)

    print(prio1, prio2)
