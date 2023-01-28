def find_marker(text, n):
    for i, char in enumerate(text):
        if i < n-1:
            continue

        if len(set(text[i-(n-1):i+1])) == n:
            return i+1


with open("06.in") as f:
    buffer = f.read()
    print(find_marker(buffer, 4))
    print(find_marker(buffer, 14))