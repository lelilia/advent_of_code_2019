"""
Advent of Code 2019
--- Day 4: Secure Container ---
"""

START = 245318
STOP = 765747


def criteria_1(password):
    return len(password) == 6


def criteria_3(password, part=1):
    part_1 = part_2 = False

    for i in range(5):
        if part_1 and part_2:
            return part_1, part_2
        if password[i] == password[i + 1]:
            part_1 = True
            part = password[max(0, i - 1) : min(i + 2, 5) + 1]
            if len(set(part)) == len(part) - 1:
                part_2 = True
    return part_1, part_2


def criteria_4(password):
    for i in range(5):
        if int(password[i]) > int(password[i + 1]):
            return False
    return True


def password_is_valid(password):

    if not criteria_1(password):
        return False, False

    if not criteria_4(password):
        return False, False

    part_1, part_2 = criteria_3(password)

    return part_1, part_2


def solve(start, stop):
    part_1 = part_2 = 0
    for password in range(start, stop + 1):
        valid_1, valid_2 = password_is_valid(str(password))
        if valid_1:
            part_1 += 1
        if valid_2:
            part_2 += 1

    print("Part 1:", part_1)
    print("Part 2:", part_2)


solve(START, STOP)


assert (password_is_valid("111111")) == (True, False)
assert (password_is_valid("111122")) == (True, True)
assert (password_is_valid("123444")) == (True, False)
assert (password_is_valid("112233")) == (True, True)
