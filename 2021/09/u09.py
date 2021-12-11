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

    def load_hmap(self, lines:str):
        for line in lines:
            # str -> list of ints e.g. '123' -> [1,2,3]
            self.hmap.append(list(map(int, list(line))))

    def adjanced(self, x:int, y:int):
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

    def is_low_point(self, x:int, y:int):
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

    def basin_walk(self, minheight:int, x:int, y:int, maxheight=9):
        """ walk only uphill, do not touch limit, do noy walk outside of the map area """
        # map low boundary check
        if x<0 or y<0:
            return None
        # map high boundary check
        if x>=len(self.hmap[0]) or y>=len(self.hmap):
            return None
        # only walk uphill and bellow limit
        height = self.hmap[y][x]
        if not minheight < height < maxheight:
            return None
        # result
        r = { (x,y) }
        # walk
        east = self.basin_walk(height, x+1,y)
        if east: r.update(east)
        west = self.basin_walk(height, x-1,y)
        if west: r.update(west)
        south = self.basin_walk(height, x,y+1)
        if south: r.update(south)
        north = self.basin_walk(height, x,y-1)
        if north: r.update(north)
        # everything ok, return height
        return r

    def basin_area(self, x:int, y:int):
        """ area surrounded by +1, 9 doesn't count  """
        w = self.basin_walk(-1, x, y)
        return len(w)

    def find_basins_area(self):
        """ find low-points """
        area = []
        for y in range(len(self.hmap)):
            for x in range(len(self.hmap[0])):
                if self.is_low_point(x,y):
                    a = self.basin_area(x,y)
                    area.append(a)
        return area

    def mult_3_biggest(self, bas:list):
        mult = 1
        for a in sorted(bas)[-3:]:
            mult *= a
        return mult

    def task_a(self, input:list):
        """ task A """
        self.load_hmap(input)
        lp = self.find_low_points()
        return self.risk_level(lp)

    def task_b(self, input:list):
        """ task B """
        self.load_hmap(input)
        basins = self.find_basins_area()
        return self.mult_3_biggest(basins)

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

# ========
#  Task B
# ========

# test cases
testcase_b(Floor(), testdata,  1134)

# 1122700
testcase_b(Floor(),   None,    1122700)
