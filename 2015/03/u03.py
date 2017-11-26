#!/usr/bin/env python

__motd__ = '--- Day 3: Perfectly Spherical Houses in a Vacuum ---'

__url__ = 'http://adventofcode.com/2015/day/3'


verbose = 0


class Position:

    def __init__(self):
        self.visited = []
        self.visit(0,0)
	  
    def visit(self, x, y):
        self.x = x
        self.y = y
        if (x,y) in self.visited:
            if verbose: print "(%d,%d) already visited" % (x,y)
            return
        self.visited.append((x,y))
        if verbose: print self.visited
                    
    def count_visited(self):
        return len(self.visited)
          
    def move_north(self):
        return self.visit(self.x, self.y+1)

    def move_south(self):
        return self.visit(self.x, self.y-1)

    def move_east(self):
        return self.visit(self.x+1, self.y)

    def move_west(self):
        return self.visit(self.x-1, self.y)

    def instructions(self, s):
        for step in s:
            if verbose: print "step=",step
            if step == '^': self.move_north()
            if step == 'v': self.move_south()
            if step == '>': self.move_east()
            if step == '<': self.move_west()


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    p = Position()
    p.instructions(input)
    r = p.count_visited()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print


# ========
#  Task A
# ========

# test cases
testcase('>',          2)
testcase('^>v<',       4)
testcase('^v^v^v^v^v', 2)

data = __file__.replace('.py', '.input')
p = Position()
with open(data) as f:
    for line in f:
        if not line: continue
        p.instructions(line)
# 2565
print 'Task A input file:',data,'Result:',p.count_visited()
print

