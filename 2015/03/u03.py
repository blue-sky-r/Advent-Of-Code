#!/usr/bin/env python

__motd__ = '--- Day 3: Perfectly Spherical Houses in a Vacuum ---'

__url__ = 'http://adventofcode.com/2015/day/3'


verbose = 0


class Position:

    def __init__(self, members=1):
        self.visited = []
        self.pos = [(0,0) for i in range(members+1)]
        for i in range(members):
            self.visit((0,0), i)
	  
    def visit(self, xy, member):
        self.pos[member] = xy
        if xy in self.visited:
            if verbose: print "(%d,%d) already visited" % (xy[0],xy[1])
            return
        self.visited.append(xy)
        if verbose: print self.visited
                    
    def count_visited(self):
        return len(self.visited)
          
    def move_north(self, member):
        x,y = self.pos[member]
        return self.visit((x,y+1), member)

    def move_south(self, member):
        x,y = self.pos[member]
        return self.visit((x,y-1), member)

    def move_east(self, member):
        x,y = self.pos[member]
        return self.visit((x+1,y), member)

    def move_west(self, member):
        x,y = self.pos[member]
        return self.visit((x-1,y), member)

    def instructions(self, s, members=1):
        member = 0
        for step in s:
            if verbose: print "step=",step,", member=",member
            if step == '^': self.move_north(member)
            if step == 'v': self.move_south(member)
            if step == '>': self.move_east(member)
            if step == '<': self.move_west(member)
            member += 1
            if member>members-1: member=0


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    p = Position()
    p.instructions(input, 2 if task_b else 1)
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

# ========
#  Task B
# ========

testcase('^>',          3, task_b=True)
testcase('^>v<',        3, task_b=True)
testcase('^v^v^v^v^v', 11, task_b=True)

p = Position()
with open(data) as f:
    for line in f:
        if not line: continue
        p.instructions(line, members=2)

# 2639
print 'Task B input file:',data,'Result:',p.count_visited()
print

