def update_tail(head_x, head_y, tail_x, tail_y):
    del_y = head_y - tail_y
    del_x = head_x - tail_x
    if abs(del_y) == 2:
        tail_y += del_y//2
        if abs(del_x) == 1:
            tail_x = head_x
    if abs(del_x) == 2:
        tail_x += del_x//2
        if abs(del_y) == 1:
            tail_y = head_y

    return tail_x, tail_y


with open("09.in") as f:
    x = [0]*10
    y = [0]*10
    visited_1 = set()
    visited_2 = set()

    for line in f:
        instr, dist = line.split()
        dist = int(dist)

        for _ in range(dist):
            # update head
            if instr == "U":
                y[0] += 1
            elif instr == "D":
                y[0] -= 1
            elif instr == "R":
                x[0] += 1
            elif instr == "L":
                x[0] -= 1

            for head in range(9):
                x[head+1], y[head+1] = update_tail(x[head], y[head], x[head+1], y[head+1])
            visited_1.add((x[1], y[1]))
            visited_2.add((x[9], y[9]))

    print(len(visited_1))
    print(len(visited_2))
