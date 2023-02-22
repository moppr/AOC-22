with open("11.in") as f:
    monkeys = f.read().split("\n\n")
    monkey_items = {}
    monkey_inspects = {}
    part = 2
    stress_reduction = 1

    for round_no in range(21 if part == 1 else 10001):
        for monkey in monkeys:
            monkey_no, starting, operation, test, true_action, false_action = monkey.split("\n")
            monkey_no = int(monkey_no[-2])
            starting = [int(x) for x in starting[18:].split(", ")]
            operation = " ".join(operation.split()[-2:])
            test = int(test.split()[-1])
            true_action = int(true_action.split()[-1])
            false_action = int(false_action.split()[-1])

            if round_no == 0:
                monkey_items[monkey_no] = starting
                monkey_inspects[monkey_no] = 0
                stress_reduction *= test
                continue

            while monkey_items[monkey_no]:
                item = monkey_items[monkey_no].pop(0)
                item = eval(str(item) + operation.replace("old", str(item)))
                item = (item // 3) if part == 1 else (item % stress_reduction)
                monkey_items[true_action if item % test == 0 else false_action].append(item)
                monkey_inspects[monkey_no] += 1

    inspects_sorted = sorted(monkey_inspects.values())[-2:]
    print(inspects_sorted[0] * inspects_sorted[1])