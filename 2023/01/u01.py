#!/usr/bin/env python3

__day__  = 1

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-01'

verbose = 0


class Calibration:

    def __init__(self):
        pass

    def firstdigit(self, line: str) -> str:
        """ the first digit from line """
        for c in line:
            if c.isdigit():
                return c

    def lastdigit(self, line: str) -> str:
        """ the lst digit from line """
        for c in line[::-1]:
            if c.isdigit():
                return c

    def linevalue(self, line: str) -> int:
        """ combine the first and last digit """
        val = 10 * int(self.firstdigit(line)) + int(self.lastdigit(line))
        return val

    def task_a(self, input: list):
        """ task A """
        vals = [ self.linevalue(line) for line in input ]
        return sum(vals)

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
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Calibration(), testdata,  142)

# 54632
testcase_a(Calibration(),   None,     54632)

# ========
#  Task B
# ========

# test cases
#testcase_b(C(), testdata,  2)

# 2
#testcase_b(C(),   None,    2)
