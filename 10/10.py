def signal(cyc_no, x_val):
    return 0 if (cyc_no - 20) % 40 != 0 else cyc_no * x_val


def draw(cyc_no, x_val):
    pos = (cyc_no - 1) % 40
    result = "█" if abs(x_val - pos) <= 1 else " "
    if cyc_no % 40 == 0:
        result += "\n"
    return result


def do_cycle():
    global cycle
    global signal_sum
    global image
    cycle += 1
    signal_sum += signal(cycle, x)
    image += draw(cycle, x)


with open("10.in") as f:
    x = 1
    cycle = 0
    signal_sum = 0
    image = ""
    for line in f:
        line = line.split()
        if len(line) == 1:
            instr = line[0]
        elif len(line) == 2:
            instr, val = line

        if instr == "noop":
            do_cycle()
        elif instr == "addx":
            for _ in range(2):
                do_cycle()
            x += int(val)

    print(signal_sum)
    print(image)
