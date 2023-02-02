

with open("sometext.txt", "r") as file:
    read_lines = file.readlines()
    position = 2
    if position >= 0 and position < len(read_lines):
        read_lines[position] = "hertion"
    print(file.read())
    print()