"""
Advent of Code 2019
--- Day 3: Crossed Wires ---
"""

with open("3.input") as f:
    input = f.readlines()

seen = {}

min_crossing = 999999
min_crossing_steps = 9999999999


def visit_coords(x, y, steps):
    global min_crossing, min_crossing_steps
    if (x, y) not in seen:
        seen[x, y] = (wire, steps)
    else:
        if seen[x, y][0] != wire:
            min_crossing = min(min_crossing, abs(x) + abs(y))
            min_crossing_steps = min(min_crossing_steps, seen[x, y][1] + steps)


for wire, line in enumerate(input):
    x = y = steps = 0
    line = line.strip()
    for code in line.split(","):
        direction, distance = code[0], int(code[1:])
        if direction == "R":
            for i in range(distance):
                x += 1
                steps += 1
                visit_coords(x, y, steps)
        elif direction == "L":
            for i in range(distance):
                x -= 1
                steps += 1
                visit_coords(x, y, steps)
        elif direction == "U":
            for i in range(distance):
                y -= 1
                steps += 1
                visit_coords(x, y, steps)
        elif direction == "D":
            for i in range(distance):
                y += 1
                steps += 1
                visit_coords(x, y, steps)
        else:
            print("something went wrong")

print("Part 1:", min_crossing)
print("Part 2:", min_crossing_steps)
