#!/usr/bin/env python3

__day__  = 5

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class HydroMap:

    def __init__(self, size=10):
        self.data = {}
        self.size = size

    def print(self, zero='.'):
        for row in range(self.size):
            print(''.join([ self.chr_xy((col,row))  for col in range(self.size) ]))
        print()

    def chr_xy(self, xy:tuple, zero='.'):
        c = self.data.get(xy, 0)
        if c == 0: return '%s ' % zero
        return '%d ' % c

    def get_xy(self, xy:tuple):
        return self.data.get(xy, 0)

    def add_xy_val(self, xy: tuple, val:int):
        self.data[xy] = self.get_xy(xy) + val

    def add_str_line(self, line: str, hvonly=True, sep=' -> '):
        """ x1,y1 -> x2,y2 H/V only - limit to Horizontal / Vertical lines"""
        x1y1, _, x2y2 = line.partition(sep)
        # startpoint
        x1,y1 = map(int, x1y1.split(','))
        # endpoint
        x2,y2 = map(int, x2y2.split(','))
        # str -> int
        return self.add_line((x1,y1), (x2,y2), hvonly)

    def add_line(self, xy1:tuple, xy2:tuple, hvonly=True, val=1):
        deltax, deltay = xy2[0] - xy1[0], xy2[1] - xy1[1]
        # exit if H/V required and not H or V line
        if hvonly and deltax != 0 and deltay != 0:
            return False
        # start from startpoint
        x, y = xy1[0], xy1[1]
        while True:
            self.add_xy_val((x,y), val)
            # did ew reachj endpoint ?
            if x == xy2[0] and y == xy2[1]:
                break
            # move by sign(delta) = delta//abs(delta)
            if deltax:
                x += deltax // abs(deltax)
            if deltay:
                y += deltay // abs(deltay)
        return True


class Hydro:

    def __init__(self, size=10):
        self.hmap = HydroMap(size)

    def count_threshold(self, threshold=2):
        """ count values >= threshold """
        selected = [ self.hmap.get_xy(xy) for xy in self.hmap.data if self.hmap.get_xy(xy) >= threshold ]
        return len(selected)

    def process_input(self, input: list, hvonly=False):
        for line in input:
            r = self.hmap.add_str_line(line, hvonly)
            if verbose:
                print(line, 'ok' if r else 'ignored')
                self.hmap.print()

    def task_a(self, input: list):
        """ task A - Horizontal / Vertial lines only"""
        self.process_input(input, hvonly=True)
        return self.count_threshold()

    def task_b(self, input):
        """ task B """
        self.process_input(input, hvonly=False)
        return self.count_threshold()


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
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2       
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Hydro(), testdata,  5)

# 4421
testcase_a(Hydro(),   None,   4421)

# ========
#  Task B
# ========

# test cases
testcase_b(Hydro(), testdata,  12)

# 18674
testcase_b(Hydro(),   None,    18674)
