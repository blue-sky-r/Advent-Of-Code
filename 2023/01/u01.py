#!/usr/bin/env python3

__day__  = 1

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-01'

verbose = 0


class Calibration:

    def __init__(self, tx: dict):
        self.tx = tx

    def firstdigit(self, line: str) -> int:
        """ the first digit from line """
        for c in line:
            v = self.tx.get(c)
            if v is not None:
                return v

    def lastdigit(self, line: str) -> int:
        """ the lst digit from line """
        for c in line[::-1]:
            v = self.tx.get(c)
            if v is not None:
                return v

    def linevalue(self, line: str) -> int:
        """ combine the first and last digit """
        val = 10 * self.firstdigit(line) + self.lastdigit(line)
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

# translator '0' -> 0
tx = { chr(ord('0') + i):i for i in range(0, 10) }

# test cases
testcase_a(Calibration(tx = tx), testdata,  142)

# 54632
testcase_a(Calibration(tx = tx),   None,     54632)

# ========
#  Task B
# ========

# test cases
#testcase_b(C(), testdata,  2)

# 2
#testcase_b(C(),   None,    2)
