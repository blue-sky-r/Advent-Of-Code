#!/usr/bin/env python3

__motd__ = "--- Day 17: Chronospatial Computer ---"

__url__ = "http://adventofcode.com/2024/day/17"

verbose = 0


class Chrono:

    def __init__(self):
        self.reg = {"A": 0, "B": 0, "C": 0}
        self.pc = 0
        self.mcode = {
            0: self._adv,
            1: self._bxl,
            2: self._bst,
            3: self._jnz,
            4: self._bxc,
            5: self._out,
            6: self._bdv,
            7: self._cdv,
        }
        self.output = []

    def _combo_op(self, op):
        """combo operand"""
        if 0 <= op <= 3:
            return op
        if op == 4:
            return self.reg["A"]
        if op == 5:
            return self.reg["B"]
        if op == 6:
            return self.reg["C"]

    def _adv(self, op):
        """A <- int(A / 2^op)"""
        self.reg["A"] = int(self.reg["A"] / 2 ** self._combo_op(op))
        return

    def _bxl(self, op):
        """B <- B xor op"""
        self.reg["B"] = self.reg["B"] ^ op
        return

    def _bst(self, op):
        """B <- op mod 8"""
        self.reg["B"] = self._combo_op(op) % 8
        return

    def _jnz(self, op):
        """jmp op if A != 0"""
        if self.reg["A"] == 0:
            return
        self.pc = op
        return

    def _bxc(self, op):
        """B <- B xor C"""
        self.reg["B"] = self.reg["B"] ^ self.reg["C"]
        return

    def _out(self, op):
        """print op mod 8"""
        v = self._combo_op(op) % 8
        if verbose:
            print(v, end=",")
        self.output.append(v)
        return

    def _bdv(self, op):
        """B <- int(A / 2^op)"""
        self.reg["B"] = int(self.reg["A"] / 2 ** self._combo_op(op))
        return

    def _cdv(self, op):
        """C <- int(A / 2^op)"""
        self.reg["C"] = int(self.reg["A"] / 2 ** self._combo_op(op))
        return

    def parseinput(self, input):
        input = input if type(input) == list else input.strip().splitlines()
        for line in input:
            if line.startswith("Register"):
                _, reg, val = line.split()
                reg = reg[0]
                self.reg[reg] = int(val)
            if line.startswith("Program: "):
                prog = [int(m) for m in line.replace("Program: ", "").split(",")]
        return prog

    def exec(self, prog):
        self.pc = 0
        while self.pc < len(prog):
            ins, op = prog[self.pc], prog[self.pc + 1]
            self.pc += 2
            self.mcode[ins](op)
        return ",".join([str(i) for i in self.output])

    def task_a(self, input):
        """task A"""
        prog = self.parseinput(input)
        res = self.exec(prog)
        return res

    def task_b(self, input):
        """task B"""
        return


def testcase(sut, input, result, task_b=False):
    """testcase verifies if input returns result"""
    # read default input file
    if input is None:
        data = __file__.replace(".py", ".input")
        with open(data) as f:
            input = [line.strip() for line in f]
    #
    print(f"TestCase {"B" if task_b else "A"} ", end="")
    print(f"for input: {data if 'data' in vars() else input}", end="")
    print(f"\t expected result: {result} ", end="")
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print(f"got: {r} \t {'[ OK ]' if r == result else '[ ERR ]'}")
    print()


# ========
#  Task A
# ========

input = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
# test cases
testcase(Chrono(),  input,  '4,6,3,5,6,3,5,2,1,0')

# 7,1,5,2,4,0,7,6,1
testcase(Chrono(), None, "7,1,5,2,4,0,7,6,1")
