#!/usr/bin/env python3

__day__  = 9

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Floor:

    def __init__(self):
        """ """
        # height-map - where 9 is the highest and 0 is the lowest
        self.hmap = []

    def load_hmap(self, lines: str):
        for line in lines:
            self.hmap.append(list(map(int, list(line))))

    def adjanced(self, x: int, y: int):
        adj = []
        # x has asj. right
        if x < len(self.hmap[0])-1:
            adj.append(self.hmap[y][x+1])
        # x has adj. left
        if x > 0:
            adj.append(self.hmap[y][x-1])
        # y has adj. bottom
        if y < len(self.hmap)-1:
            adj.append(self.hmap[y+1][x])
        # x has adj. top
        if y > 0:
            adj.append(self.hmap[y-1][x])
        return adj

    def is_low_point(self, x: int, y: int):
        """ low-points - the locations that are lower than any of its adjacent locations """
        h = self.hmap[y][x]
        adj = self.adjanced(x, y)
        return all([ h < a for a in adj ])

    def find_low_points(self):
        """ find low-points """
        lp = []
        for y in range(len(self.hmap)):
            for x in range(len(self.hmap[0])):
                if self.is_low_point(x,y):
                    h = self.hmap[y][x]
                    lp.append(h)
        return lp

    def risk_level(self, lp: list):
        return sum([h+1 for h in lp])

    def task_a(self, input: list):
        """ task A """
        self.load_hmap(input)
        lp = self.find_low_points()
        return self.risk_level(lp)

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
2199943210
3987894921
9856789892
8767896789
9899965678          
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Floor(), testdata,  15)

# 535
testcase_a(Floor(),   None,   535)

