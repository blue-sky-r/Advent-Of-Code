#!/usr/bin/env python

__motd__ = '--- Day 1: No Time for a Taxicab ---'

__url__ = 'http://adventofcode.com/2016/day/1'

verbose = 0

class Map:

    def __init__(self, only_once=False):
        self.track = []
        self.setxy(0, 0)
        self.face = 'N'
        self.only_once = only_once

    def setxy(self, x, y):
        self.x = x
        self.y = y
        self.track.append((x,y))

    def turn(self, rl):
        " change facing direction "
        if self.face == 'N':
            if rl == 'R': self.face = 'E'
            if rl == 'L': self.face = 'W'
            return
        if self.face == 'S':
            if rl == 'R': self.face = 'W'
            if rl == 'L': self.face = 'E'
            return
        if self.face == 'E':
            if rl == 'R': self.face = 'S'
            if rl == 'L': self.face = 'N'
            return
        if self.face == 'W':
            if rl == 'R': self.face = 'N'
            if rl == 'L': self.face = 'S'
            return

    def walk(self, steps=1):
        " returns new (x,y) "
        if self.face == 'N':
            return self.x, self.y + steps
        if self.face == 'S':
            return self.x, self.y - steps
        if self.face == 'E':
            return self.x + steps, self.y
        if self.face == 'W':
            return self.x - steps, self.y
        return self.x, self.y

    def distance_xy(self):
        return abs(self.x) + abs(self.y)

    def instruction(self, str):
        " returns True if current location is visited twice "
        dir = str[0]
        cnt = str[1:]
        return self.goto(dir, int(cnt))

    def sequence(self, seq, sep=','):
        " follow the sequence, optionaly returns true if the last location was visited twice "
        for step in seq.split(sep):
            if self.instruction(step.strip()) and self.only_once:
                return True

    def goto(self, dir, steps):
        " return True if current location is visited 2nd time "
        self.turn(dir)
        for step in range(1, steps+1):
            x,y = self.walk()
            visited = self.already_visited(x,y)
            self.setxy(x, y)
            if self.only_once and visited:
                return True
        return False

    def already_visited(self, x, y):
        return (x,y) in self.track


def testcase(input, result, only_once=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if only_once else 'A',
    print "for input:",input,"\t expected result:",result,
    map = Map(only_once)
    map.sequence(input)
    r = map.distance_xy()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    if verbose: print "Trace:",map.track
    print

# ========
#  Task A
# ========

# test cases
testcase('R2, L3',          5)
testcase('R2, R2, R2',      2)
testcase('R5, L5, R5, R3', 12)

data = __file__.replace('.py', '.input')
map  = Map()
with open(data) as f:
    for line in f:
        if not line: continue
        map.sequence(line)
# 291
print 'Task A input file:',data,'Result:',map.distance_xy()
if verbose: print "Trace:",map.track
print

# ========
#  Task B
# ========

# test cases
testcase('R8, R4, R4, R8', 4, only_once=True)

map  = Map(only_once=True)
with open(data) as f:
    for line in f:
        if not line: continue
        if map.sequence(line): break
# 159
print 'Task B input file:',data,'Result:',map.distance_xy()
if verbose: print "Trace:",map.track
