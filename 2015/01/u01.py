#!/usr/bin/env python

__motd__ = '--- Day 1: Not Quite Lisp ---'

__url__ = 'http://adventofcode.com/2015/day/1'


class Elevator:

    def __init__(self, startpos=0):
        self.pos = startpos
        self.idx = 0

    def instruction(self, i):
        self.idx += 1
        if i == '(': self.pos += 1
        if i == ')': self.pos -= 1

    def follow(self, str, stop_at_basement=False):
        self.step = 0
        for i in str:
            self.instruction(i)
            self.step += 1
            if stop_at_basement and self.pos<0:
                return self.step
        return self.pos


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    ele = Elevator()
    r = ele.follow(input, stop_at_basement=task_b)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
testcase('(())',     0)
testcase('()()',     0)
testcase('))(((((',  3)
testcase('())',     -1)
testcase('))(',     -1)
testcase(')))',     -3)
testcase(')())())', -3)

data = __file__.replace('.py', '.input')
ele  = Elevator()
with open(data) as f:
    for line in f:
        if not line: continue
        ele.follow(line.strip())
# 232
print 'Task A input file:',data,'Result:',ele.pos
print

# ========
#  Task B
# ========

# test cases
testcase(')((((',     1, True)
testcase('()())(((',  5, True)

data = __file__.replace('.py', '.input')
ele  = Elevator()
with open(data) as f:
    for line in f:
        if not line: continue
        ele.follow(line.strip(), stop_at_basement=True)
# 1783
print 'Task B input file:',data,'Result:',ele.step
print
