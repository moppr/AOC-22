with open("05.in") as f:
    a, b = f.read().split("\n\n")

    stacks = {}
    for line in a.split("\n")[:-1]:
        stack = 0
        for i in range(1, len(line), 4):
            stack += 1
            char = line[i]
            if char == ' ':
                continue

            if stack in stacks:
                stacks[stack].insert(0, char)
            else:
                stacks[stack] = [char]

    for line in b.split("\n"):
        m, f, t = [int(x) for x in line.split()[1::2]]

        for _ in range(m):
            stacks[t].append(stacks[f].pop())

    for key in sorted(stacks.keys()):
        print(stacks[key][-1], end='')
    print()
