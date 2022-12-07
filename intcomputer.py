
class Intcomputer:
    def __init__(self, filename):
        self.code_original = self.get_input(filename)

    def get_input(self, filename):
        with open(filename, "r") as f:
            input = f.read()
            return [int(x) for x in input.split(",")]

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

    def run(self):
        i = 0
        while self.code[i] != 99:
            opcode = self.code[i]
            if opcode == 1:
                pos_1, pos_2, pos_3 = self.code[i + 1 : i + 4]
                self.code[pos_3] = self.code[pos_1] + self.code[pos_2]
                i += 4
            elif opcode == 2:
                pos_1, pos_2, pos_3 = self.code[i + 1 : i + 4]
                self.code[pos_3] = self.code[pos_1] * self.code[pos_2]
                i += 4
        return self.code[0]