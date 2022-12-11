#!/usr/bin/env python3

__day__  = 8

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class TreeMap:

    def __init__(self):
        pass

    def is_visible(self, xy):
        """ """
        x, y = xy[0], xy[1]
        dimx, dimy = self.dim[0], self.dim[1]
        # borders are visible
        if x == 0 or y == 0 or x == dimx or y == dimy:
            return True
        # left
        left = [ True if self.hmap[xy] > self.hmap[(xx,y)] else False for xx in range(x) ]
        visible_from_left = all(left)
        # right
        right = [ True if self.hmap[xy] > self.hmap[(xx,y)] else False for xx in range(x+1, dimx) ]
        visible_from_right = all(right)
        # up
        up = [ True if self.hmap[xy] > self.hmap[(x,yy)] else False for yy in range(y) ]
        visible_from_up = all(up)
        # down
        down = [ True if self.hmap[xy] > self.hmap[(x,yy)] else False for yy in range(y+1, dimy) ]
        visible_from_down = all(down)
        #
        return visible_from_left or visible_from_right or visible_from_up or visible_from_down

    def create_map(self, input):
        """ """
        self. hmap = {}
        for y, line in enumerate(input):
            for x, height in enumerate(line):
                self.hmap[ (x,y) ] = height
        self.dim = (x+1,y+1)

    def task_a(self, input: list):
        """ task A """
        self.create_map(input)
        visible = [ (x,y) for x in range(self.dim[0]) for y in range(self.dim[1]) if self.is_visible( (x,y) ) ]
        v = len(visible)
        return v

    def task_b(self, input: list):
        """ task B """
        return None


def testcase_a(sut, input, result, trim=str.strip):
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

def testcase_b(sut, input, result, trim=str.strip):
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
30373
25512
65332
33549
35390
"""

# ========
#  Task A
# ========

# test cases
testcase_a(TreeMap(), testdata,  21)

# 1733
testcase_a(TreeMap(),   None,  1733)

