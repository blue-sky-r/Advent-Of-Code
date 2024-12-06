#!/usr/bin/env python3

__motd__ = '--- Day 3: Mull It Over ---'

__url__ = 'http://adventofcode.com/2024/day/3'

import re

verbose = 0


class CorruptedMult:

    def __init__(self, regex: str = r'mul\((\d+),(\d+)\)'):
        self.regex = regex

    def task_a(self, input):
        """ task A """
        mults = []
        for m in re.finditer(r'mul\((\d+),(\d+)\)', ''.join(input), re.MULTILINE):
            t = int(m[1]), int(m[2])
            mults.append(t)
        r = [ t[0] * t[1] for t in mults ]
        r = sum(r)
        return r

    def task_b(self, input):
        """ task B """
        return


def testcase(sut, input, result, task_b=False):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print(f"TestCase {"B" if task_b else "A"} ", end='')
    print(f"for input: {data if 'data' in vars() else input}", end='')
    print(f"\t expected result: {result} ", end='')
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print(f"got: {r} \t {'[ OK ]' if r == result else '[ ERR ]'}")
    print()

# ========
#  Task A
# ========

input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# test cases
testcase(CorruptedMult(),  input,  161)

# 173419328
testcase(CorruptedMult(),  None, 173419328)

# ========
#  Task B
# ========

# test cases
testcase(Distance(),  inputa,  31, task_b=True)

# 24931009
testcase(Distance(),  None,  24931009, task_b=True)
