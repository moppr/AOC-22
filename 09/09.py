with open("09.in") as f:
    head_x = head_y = tail_x = tail_y = 0
    visited = set()

    for line in f:
        instr, dist = line.split()
        dist = int(dist)

        for _ in range(dist):
            # update head
            if instr == "U":
                head_y += 1
            elif instr == "D":
                head_y -= 1
            elif instr == "R":
                head_x += 1
            elif instr == "L":
                head_x -= 1

            # update tail
            del_y = head_y - tail_y
            del_x = head_x - tail_x
            if abs(del_y) == 2:
                tail_y += del_y//2
                if del_x != 0:
                    tail_x = head_x
            if abs(del_x) == 2:
                tail_x += del_x//2
                if del_y != 0:
                    tail_y = head_y

            visited.add((tail_x, tail_y))

    print(len(visited))
