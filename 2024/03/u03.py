#!/usr/bin/env python3

__motd__ = "--- Day 3: Mull It Over ---"

__url__ = "http://adventofcode.com/2024/day/3"

import re

verbose = 0


class CorruptedMult:

    def __init__(self, regex: str):
        self.regex = regex

    def mults(self, input) -> list[tuple]:
        """ extract multiplicators into tuples """
        mults = []
        for m in re.finditer(self.regex, "".join(input), re.MULTILINE):
            t = int(m[1]), int(m[2])
            mults.append(t)
        return mults

    def multscond(self, input) -> list[tuple]:
        """ extract multiplicators into tuples with do/dont conditionals """
        mults, do = [], True
        for m in re.finditer(self.regex, "".join(input), re.MULTILINE):
            if m[0] == 'do()':
                do = True
                continue
            if m[0] == 'don\'t()':
                do = False
                continue
            t = int(m[1]), int(m[2])
            if do:
                mults.append(t)
        return mults

    def summults(self, mults: list) -> int:
        """ [(a,b), (c,d)] -> a*b + c*d ... """
        return sum([t[0] * t[1] for t in mults])

    def task_a(self, input):
        """task A"""
        mults = self.mults(input)
        return self.summults(mults)

    def task_b(self, input):
        """task B"""
        mults = self.multscond(input)
        return self.summults(mults)


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
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
regex = r"mul\((\d+),(\d+)\)"

# test cases
testcase(CorruptedMult(regex), input, 161)

# 173419328
testcase(CorruptedMult(regex), None, 173419328)

# ========
#  Task B
# ========

input = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
regex = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
# test cases
testcase(CorruptedMult(regex), input, 48, task_b=True)

# 90669332
testcase(CorruptedMult(regex), None, 90669332, task_b=True)
