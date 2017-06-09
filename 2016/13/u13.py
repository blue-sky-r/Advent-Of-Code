#!/usr/bin/env python

__motd__ = '--- Day 13: A Maze of Twisty Little Cubicles ---'

__url__ = 'http://adventofcode.com/2016/day/13'

verbose = 1

class Cubicle:

    def __init__(self, wall='#', openspace='.', favnum=0):
        " init symbols for wall/openspace and fav.number "
        self.wall = wall
        self.openspace = openspace
        self.favnum = favnum

    def formula(self, x, y):
        " formula "
        return x*x + 3*x + 2*x*y + y + y*y + self.favnum

    def wall_space(self, x, y):
        " get symbol wall/space from formula "
        b = self.formula(x, y)
        sym = self.wall if bin(b).count('1') % 2 else self.openspace
        return sym

    def build_map(self, sizex, sizey):
        " build entire map sizex x sizey "
        self.map = {}
        self.map_size = (sizex, sizey)
        for x in range(sizex+1):
            for y in range(sizey+1):
                self.map[(x,y)] = self.wall_space(x,y)

    def show_map(self, frm="%3s"):
        " show map "
        maxx,maxy = max(self.map)
        print
        # x coords
        print "y\\x",
        for x in range(maxx+1):
            print frm % (x % 10),
        print
        for y in range(maxy + 1):
            # y coords
            print "%3d" %y,
            for x in range(maxx+1):
                print frm % self.map[(x,y)],
            print
        print

    def fill_map(self, x, y, value=0):
        " fill recursively map point (x,y) with value "
        # cannot fill outsize the map
        if not (0 <= x <= self.map_size[0]): return False
        if not (0 <= y <= self.map_size[1]): return False
        # cannot fill wall
        if self.map[(x,y)] == self.wall: return False
        # can update value
        if self.map[(x,y)] != self.openspace:
            # do not upate the sanme or smaller value
            if self.map[(x,y)] <= value: return False
        # set point (x,y) to value
        self.map[(x,y)] = value
        # set all 4 neighbours to higher value
        self.fill_map(x+1,y, value+1)
        self.fill_map(x-1,y, value+1)
        self.fill_map(x,y+1, value+1)
        self.fill_map(x,y-1, value+1)

    def distance(self, xy):
        " get distance to point (x,y) "
        return self.map[xy]

    def locations(self, steps):
        " caout visited locations in less than steps "
        return len([ loc for loc in self.map if self.map not in [self.wall,self.openspace] and self.map[loc] <= steps ])


def testcase(favnum, point, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",favnum,"distance to",point,"\t expected result:",result,
    cb = Cubicle(favnum=favnum)
    cb.build_map(9,6)
    if verbose: cb.show_map()
    cb.fill_map(1,1)
    if verbose: cb.show_map()
    r = cb.distance(point)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    if verbose: print "Trace:",
    print

# ========
#  Task A
# ========

# test cases
testcase(10, (7,4), 11)

favnum=1352; point=(31,39)
#
cb = Cubicle(favnum=favnum)
cb.build_map(40, 40)
if verbose: cb.show_map()
cb.fill_map(1, 1)
if verbose: cb.show_map()
r = cb.distance(point)
# 90
print 'Task A input:',favnum,'Distance to point:',point,'Result:',r
print

# ========
#  Task B
# ========

steps=50
l = cb.locations(steps)
# 135
print 'Task B input:',favnum,'Locations:',l
print
