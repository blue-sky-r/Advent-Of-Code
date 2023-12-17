#!/usr/bin/env python3

__day__  = 9

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-10'

verbose = 0


class Predictor:

    def __init__(self):
        pass

    def calc_diffs(self, l: list) -> list:
        """ cacl differences """
        diff = [ b-a for a,b in zip(l,l[1:]) ]
        return diff

    def predict(self, lst: list) -> int:
        """ predict leading and trailing number for lst """
        if all([i==0 for i in lst]):
            return 0, 0
        diff = self.calc_diffs(lst)
        head, tail = self.predict(diff)
        return lst[0] - head, lst[-1] + tail

    def task_a(self, input: list):
        """ task A """
        r = []
        for line in input:
            lst = [ int(i) for i in line.split() ]
            head, tail = self.predict(lst)
            r.append(tail)
        return sum(r)

    def task_b(self, input: list):
        """ task B """
        r = []
        for line in input:
            lst = [ int(i) for i in line.split() ]
            head, tail = self.predict(lst)
            r.append(head)
        return sum(r)


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
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Predictor(), testdata,  114)

# 1819125966
testcase_a(Predictor(), None, 1819125966)

# ========
#  Task B
# ========

# test cases
testcase_b(Predictor(), testdata,  2)

# 1140
testcase_b(Predictor(),   None, 1140)
