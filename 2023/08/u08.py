#!/usr/bin/env python3

__day__  = 8

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-08'

verbose = 0


class Wasteland:

    def __init__(self):
        pass

    def walk(self, map: dict, steps: str, act: str, end: str) -> list:
        """ walk steps """
        path, stepidx = [], 0
        while act != end:
            left, right = map[act]
            step, stepidx = steps[stepidx], (stepidx + 1) % len(steps)
            if step == 'L':
                act = left
            if step == 'R':
                act = right
            path.append(act)
        return path

    def parse_map(self, input: list):
        """ """
        map, steps = {}, ''
        for line in input:
            if len(line) == 0:
                continue
            if len(steps) == 0:
                steps = line
                continue
            # AAA = (BBB, CCC)
            name, lr = line.split(' = ')
            # remove brackets
            lr = lr[1:-1]
            left, right = lr.split(', ')
            map[name] = (left, right)
        return map, steps

    def task_a(self, input: list):
        """ task A """
        map, steps = self.parse_map(input)
        path = self.walk(map, steps, 'AAA', 'ZZZ')
        return len(path)

    def task_b(self, input: list):
        """ task B """
        return None


def testcase_a(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_b(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()


# ======
#  MAIN
# ======

print()
print(__motd__, __url__)
print()

testdata = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Wasteland(), testdata,  2)

testdata = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

# test cases
testcase_a(Wasteland(), testdata,  6)

# 19241
testcase_a(Wasteland(), None, 19241)

