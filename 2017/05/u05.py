#!/usr/bin/env python

__motd__ = '--- Day 5: A Maze of Twisty Trampolines, All Alike ---'

__url__ = 'http://adventofcode.com/2017/day/5'


verbose = 0


class Jump:

    def __init__(self, task_b=False):
        self.pc     = 0
        self.steps  = 0
        self.program = []
        self.task_b = task_b

    def jump(self):
        offset = self.program[self.pc]
        if verbose:
            print "pc:",self.pc,"offset(",offset,") steps:",self.steps,"prog:",self.program
        if self.task_b and offset>=3:
            self.program[self.pc] -= 1
        else:
            self.program[self.pc] += 1
        self.pc += offset
        self.steps += 1

    def inside(self):
        return 0 <= self.pc < len(self.program)

    def execute(self, lst):
        self.program = lst
        while self.inside():
            self.jump()
        return self.steps


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    j = Jump(task_b)
    r = j.execute(input)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

testcase([ 0, 3, 0, 1, -3 ],  5)

data = __file__.replace('.py', '.input')
j = Jump()
prog = []
with open(data) as f:
    for line in f:
        if not line: continue
        prog.append(int(line.strip()))
# 318883
print 'Task A input file:',data,'Result:',j.execute(prog)
print

# ========
#  Task B
# ========

testcase([ 0, 3, 0, 1, -3 ],  10, task_b=True)

j = Jump(task_b=True)
prog = []
with open(data) as f:
    for line in f:
        if not line: continue
        prog.append(int(line.strip()))
# 23948711
print 'Task B input file:',data,'Result:',j.execute(prog)
print
