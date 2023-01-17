with open("01.in") as f:
    elves = [[int(y) for y in x.split()] for x in f.read().split("\n\n")]

    most = -1
    for i, elf in enumerate(elves):
        cal = sum(elf)
        if cal > most:
            most = cal

    print(most)
