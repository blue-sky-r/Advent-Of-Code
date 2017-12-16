#!/usr/bin/env python

__motd__ = '--- Day 11: Hex Ed ---'

__url__ = 'http://adventofcode.com/2017/day/11'


verbose = 1


class HexGrid:

    def __init__(self):
        self.pos = (0,0)

    def dx_dy(self, dx, dy):
        self.pos = (self.pos[0]+dx, self.pos[1]+dy)
        
    def move(self, dir):
        if dir == 'n': self.dx_dy(0,+2)
        if dir == 's': self.dx_dy(0,-2)
        if dir == 'ne': self.dx_dy(+1,+1)
        if dir == 'se': self.dx_dy(+1,-1)
        if dir == 'nw': self.dx_dy(-1,+1)
        if dir == 'sw': self.dx_dy(-1,-1)

    def run(self, str):
        maxdist = 0
        for dir in str.split(','):
            if verbose: print dir,self.pos,'->',
            self.move(dir)
            if verbose: print self.pos
            maxdist = max(self.dist(), maxdist)
        return self.dist(), maxdist
                
    def dist(self):
        ax, ay = abs(self.pos[0]), abs(self.pos[1])
        diagonal, orthogonal = min(ax,ay), max(ax,ay)
        return diagonal + abs(ay - diagonal)/2


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    h = HexGrid()
    a,b = h.run(input)
    r = b if task_b else a
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========


testcase('ne,ne,ne', 		3)
testcase('ne,ne,sw,sw', 	0)
testcase('ne,ne,s,s', 		2)
testcase('se,sw,se,sw,sw', 	3)

data = __file__.replace('.py', '.input')
h = HexGrid()
with open(data) as f:
    for line in f:
        r = h.run(line.strip())

# 784, 1558
#
print 'Task A/B input file:',data,'Result A/B:',r
