def signal(cyc_no, x_val):
    return 0 if (cyc_no - 20) % 40 != 0 else cyc_no * x_val


with open("10.in") as f:
    x = 1
    cycle = 0
    signal_sum = 0
    for line in f:
        line = line.split()
        if len(line) == 1:
            instr = line[0]
        elif len(line) == 2:
            instr, val = line

        if instr == "noop":
            cycle += 1
            signal_sum += signal(cycle, x)
        elif instr == "addx":
            cycle += 1
            signal_sum += signal(cycle, x)
            cycle += 1
            signal_sum += signal(cycle, x)
            x += int(val)

    print(signal_sum)