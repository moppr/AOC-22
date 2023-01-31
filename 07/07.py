with open("07.in") as f:
    directories = {"/": 0}
    dirs = []
    current_dirs = []

    for line in f:
        if line.startswith("$ cd"):
            d = line.split()[-1]
            if d == "..":
                dirs.pop()
                current_dirs.pop()
            else:
                current_dirs.append("_".join(dirs+[d]))
                dirs.append(d)
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            pass
        else:  # starts with an int
            size, filename = line.split()
            size = int(size)
            for d in current_dirs:
                if d in directories:
                    directories[d] += size
                else:
                    directories[d] = size

    total = 0
    for s in directories.values():
        if s <= 100000:
            total += s
    print(total)
