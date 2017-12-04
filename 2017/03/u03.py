#!/usr/bin/env python

__motd__ = '--- Day 3: Spiral Memory ---'

__url__ = 'http://adventofcode.com/2017/day/3'


verbose = 0


# -2.2 /17  -1.2/16  0.2/15  1.2/14  2.2/ 13 3.2 /30
# -2.1 /18  -1.1 /5  0.1 /4  1.1/3   2.1 /12 3.1 /29
# -2.0 /19  -1.0 /6  0.0 /1  1.0/2   2.0 /11 3.0 /28
# -2.-1/20  -1.-1/7  0.-1/8  1.-1/9  2.-1/10 3.-1/27
# -2.-2/21  -1.-2/22 0.-2/23 1.-2/24 2.-2/25 3.-2/26


class Memory:

    def __init__(self):
        self.mem = {}
        self.add( (0,0), 1 )

    def add(self, xy, val):
        if verbose : print "cell %s=%d " % (xy, val)
        self.mem[xy] = val

    def manhattan_dist(self, limit):
        val = 2
        for xy in self.get_xy():
            self.add(xy, val)
            if val >= limit: return abs(xy[0]) + abs(xy[1])
            val += 1

    def get_xy(self):
        dir = [(+1, 0), (0, +1), (-1, 0), (0, -1)]
        diridx = 0
        reuse = 2
        x,y = 0,0
        val = 1
        for steps in range(1,9999):
            for r in range(reuse):
                for s in range(steps):
                    dx,dy = dir[diridx]
                    x += dx
                    y += dy
                    yield x, y
                diridx = (diridx + 1) % len(dir)

    def fill_sum(self, limit):
        for xy in self.get_xy():
            val = self.sum_adjanced(xy)
            self.add(xy, val)
            if val > limit: return val
            val += 1

    def sum_adjanced(self, xy):
        adj = [ self.mem.get(xy,0) for xy in self.adjanced_xy(xy) ]
        if verbose: print xy,adj
        return sum(adj)

    #  -1,1  0,1  1,1
    #  -1,0  0,0  1,0
    #  -1,-1 0,-1 1,-1
    def adjanced_xy(self, xy):
        adj = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        a = [ (xy[0]+dxy[0],xy[1]+dxy[1]) for dxy in adj ]
        return a


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    m = Memory()
    r = m.fill_sum(input)  if task_b else m.manhattan_dist(input)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

testcase(   1,  0)
testcase(  12,  3)
testcase(  23,  2)
testcase(1024, 31)

# use task_A output as testcase
data = 265149
# 438
testcase(data, 438)

# ========
#  Task B
# ========

testcase(  0,   1, task_b=True)
testcase(  1,   2, task_b=True)
testcase(  3,   4, task_b=True)
testcase(  4,   5, task_b=True)
testcase( 10,  11, task_b=True)
testcase( 58,  59, task_b=True)
testcase(146, 147, task_b=True)
testcase(361, 362, task_b=True)
testcase(805, 806, task_b=True)

# use task_B output as testcase
# 266330
testcase(data, 266330, task_b=True)
