with open("06.in") as f:
    buffer = f.read()
    for i, char in enumerate(buffer):
        if i < 3:
            continue

        if len(set(buffer[i-3:i+1])) == 4:
            print(i+1)
            break