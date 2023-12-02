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

    def linevaluedigit(self, line: str) -> int:
        """ combine the first and last digit """
        val = 10 * self.firstdigit(line) + self.lastdigit(line)
        return val

    def linefirstpos(self, line: str, substr: str) -> int:
        """ the first position of substring in line, -1 if not found """
        return line.find(substr)

    def linelastpos(self, line: str, substr: str) -> int:
        """ the first position of substring in line, -1 if nor found """
        return line.rfind(substr)

    def lineposval(self, line: str) -> dict:
        """ get dict of position -> value for all keys from translator tx """
        pos_val = {}
        for txt,val in self.tx.items():
            pos1st, posLast = self.linefirstpos(line, txt), self.linelastpos(line, txt)
            if pos1st >= 0:
                pos_val[pos1st] = val
            if posLast >= 0:
                pos_val[posLast] = val
        return pos_val

    def linevaluedesc(self, line: str) -> int:
        """ combine the first and last digit """
        pos_val = self.lineposval(line)
        firstpos, lastpos = min(pos_val), max(pos_val)
        val = 10 * pos_val[firstpos] + pos_val[lastpos]
        return val

    def task_a(self, input: list):
        """ task A """
        vals = [ self.linevaluedigit(line) for line in input ]
        return sum(vals)

    def task_b(self, input: list):
        """ task B """
        vals = [ self.linevaluedesc(line) for line in input ]
        return sum(vals)


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

# descriptive translator 'one' -> 1
tx_desc = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

# merge basic and descriptive translators
fulltx = {**tx, **tx_desc}

testdata = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

# test cases
testcase_b(Calibration(tx = fulltx), testdata,  281)

# 54019
testcase_b(Calibration(tx = fulltx),   None,  54019)
