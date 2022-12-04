"""
Advent of Code 2019
--- Day 1: The Tyranny of the Rocket Equation ---
"""


def get_input(filename):
    with open(filename, "r") as f:
        return f.readlines()


def get_fuel(mass):
    return mass // 3 - 2


def get_rec_fuel(mass):
    total_fuel = 0
    while (mass := get_fuel(mass)) > 0:
        total_fuel += mass
    return total_fuel


def solve(modules):
    total_fuel_1 = total_fuel_2 = 0
    for module in modules:
        total_fuel_1 += get_fuel(int(module))
        total_fuel_2 += get_rec_fuel(int(module))
    return total_fuel_1, total_fuel_2


input = get_input("1.input")
solution_1, solution_2 = solve(input)
print("Part 1:", solution_1)
print("Part 2:", solution_2)

# assertions
assert get_fuel(12) == 2
assert get_fuel(14) == 2
assert get_fuel(1969) == 654
assert get_fuel(100756) == 33583
assert get_rec_fuel(14) == 2
assert get_rec_fuel(1969) == 966
