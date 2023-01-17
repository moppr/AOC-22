with open("01.in") as f:
    elves = [[int(y) for y in x.split()] for x in f.read().split("\n\n")]

    top3 = [-1]*3
    for i, elf in enumerate(elves):
        cal = sum(elf)
        if cal > top3[0]:
            top3[0] = cal
            top3 = sorted(top3)

    # print(top3)
    print(top3[2])
    print(sum(top3))
