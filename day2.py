"""
Advent of Code 2019
--- Day 2: 1202 Program Alarm ---
"""

from intcomputer import Intcomputer


class Intcode(Intcomputer):

    def solve_1(self):
        self.code = self.code_original.copy()
        self.code[1] = 12
        self.code[2] = 2
        return self.run()

    def solve_2(self):
        for noun in range(100):
            for verb in range(100):
                self.code = self.code_original.copy()
                self.code[1] = noun
                self.code[2] = verb
                self.run()
                if self.code[0] == 19690720:
                    return noun * 100 + verb




t = Intcode("2.input")
print("Part 1:", t.solve_1())
print("Part 2:", t.solve_2())

