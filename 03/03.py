with open("03.in") as f:

    prio = 0
    for sack in f:
        half = len(sack)//2
        c1, c2 = sack[:half], sack[half:]

        for item in set(c1):
            if item in c2:
                prio += ord(item)-64+26 if item.isupper() else ord(item)-96
                break

    print(prio)
