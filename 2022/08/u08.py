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
        # 4 dirs
        for dx,dy in [(-1,0), (+1,0), (0,-1), (0,+1)]:
            visible = all([ self.hmap[xy] > self.hmap[(xy_)] for xy_ in self.xy_move(xy, dx, dy) ])
            if visible:
                return True
        return False

    def create_map(self, input):
        """ build height map from string matrix """
        self.hmap = {}
        for y, line in enumerate(input):
            for x, height in enumerate(line):
                self.hmap[ (x,y) ] = height
        self.dim = (x+1,y+1)

    def xy_move(self, xy, dx=0, dy=0):
        """ possible moves from position xy by direction dx/dy """
        x, y = xy[0], xy[1]
        dimx, dimy = self.dim[0], self.dim[1]
        r = []
        while dx != 0 and 0 <= x+dx < dimx:
            x += dx
            r.append( (x,y) )
        while dy != 0 and 0 <= y+dy < dimy:
            y += dy
            r.append( (x,y) )
        return r

    def can_see(self, xy, dx=0, dy=0):
        """ can see trees from xy """
        treeheight = self.hmap[xy]
        r = []
        for xy in self.xy_move(xy, dx, dy):
            height = self.hmap[xy]
            r.append(height)
            if height >= treeheight:
                break
        return r

    def scenic_score(self, xy):
        """ how many trees can see xy """
        # up
        up    = self.can_see(xy, dx=0, dy=-1)
        down  = self.can_see(xy, dx=0, dy=+1)
        left  = self.can_see(xy, dx=-1, dy=0)
        right = self.can_see(xy, dx=+1, dy=0)
        return len(up) * len(down) * len(left) * len(right)

    def task_a(self, input: list):
        """ task A """
        self.create_map(input)
        visible = [ (x,y) for y in range(self.dim[1]) for x in range(self.dim[0]) if self.is_visible( (x,y) ) ]
        v = len(visible)
        return v

    def task_b(self, input: list):
        """ task B """
        self.create_map(input)
        scoremap = [ self.scenic_score( (x,y) ) for y in range(self.dim[1]) for x in range(self.dim[0]) ]
        return max(scoremap)


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

"""
0 0  0 0 0
0 1  4 2 0
0 4  2 8 0
0 6 12 1 0
0 0  0 0 0
"""
# ========
#  Task A
# ========

# test cases
testcase_a(TreeMap(), testdata,  21)

# 1733
testcase_a(TreeMap(),   None,  1733)

# ========
#  Task B
# ========

# test cases
testcase_b(TreeMap(), testdata,    8)

# 284648
testcase_b(TreeMap(),   None, 284648)

