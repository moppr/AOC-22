with open("04.in") as f:

    c = 0
    for pair in f:
        e1, e2 = pair.split(",")
        e1 = [int(x) for x in e1.split("-")]
        e2 = [int(x) for x in e2.split("-")]

        if e1[0] <= e2[0] <= e1[1] and e1[0] <= e2[1] <= e1[1]:
            c += 1
        elif e2[0] <= e1[0] <= e2[1] and e2[0] <= e1[1] <= e2[1]:
            c += 1

    print(c)
