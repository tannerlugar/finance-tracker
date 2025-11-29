import os

if not os.path.exists("demofile.txt"):
    with open("demofile.txt", "w") as f:
        f.write("0\n")

with open("demofile.txt") as f:
    first_line = f.readline()
    remaining_lines = f.readlines()
    print(remaining_lines)
