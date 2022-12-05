#!/usr/bin/env python3

__day__  = 2

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class RockPaperScissors:

    def __init__(self):
        loss, draw, win = 0, 3, 6
        rock, paper, scissors = 1, 2, 3
        self.score = {
            # ROCK ->
            'A X': rock + draw,
            'A Y': paper + win,
            'A Z': scissors + loss,
            # PAPER ->
            'B X': rock + loss,
            'B Y': paper + draw,
            'B Z': scissors + win,
            # SCISSORS ->
            'C X': rock + win,
            'C Y': paper + loss,
            'C Z': scissors + draw
        }
        pass

    def task_a(self, input: list):
        """ task A """
        scores = [ self.score[rnd] for rnd in input ]
        return sum(scores)

    def task_b(self, input: list):
        """ task B """
        return None


def testcase_a(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.strip() for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.strip() for line in input.splitlines() ]
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
A Y
B X
C Z
"""

# ========
#  Task A
# ========

# test cases
testcase_a(RockPaperScissors(), testdata,  15)

# 12679
testcase_a(RockPaperScissors(),   None, 12679)

# ========
#  Task B
# ========

# test cases
#testcase_b(C(), testdata,  2)

# 2
#testcase_b(C(),   None,    2)
