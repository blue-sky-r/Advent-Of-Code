#!/usr/bin/env python

__motd__ = '--- Day 6: Probably a Fire Hazard ---'

__url__ = 'http://adventofcode.com/2015/day/6'


verbose = 0


class LightsB:

    def __init__(self, x=1000, y=1000, state=0):
        self.grid = []
        for i in range(x):
            self.grid.append([state for i in range(y)])

    def on(self, x,y):
        self.grid[x][y] += 1

    def off(self, x,y):
        self.grid[x][y] = max(0, self.grid[x][y]-1)

    def toggleXY(self, x,y):
        self.grid[x][y] += 2

    def total_brightness(self):
        sum = 0
        for x in range(1000):
            for y in range(1000):
                sum += self.grid[x][y]
        return sum

    def turn_on(self, xa,ya, xb,yb):
        for x in range(xa,xb+1):
            for y in range(ya,yb+1):
                self.on(x,y)

    def turn_off(self, xa,ya, xb,yb):
        for x in range(xa,xb+1):
            for y in range(ya,yb+1):
                self.off(x,y)

    def toggle(self, xa,ya, xb,yb):
        for x in range(xa,xb+1):
            for y in range(ya,yb+1):
                self.toggleXY(x,y)

    def xy(self, csv):
        x,y = map(int, csv.split(','))
        return x,y

    def action(self, cmd):
        if cmd.startswith('turn on '):
            a,_,b = cmd.replace('turn on ','').partition(' through ')
            xa,ya = self.xy(a)
            xb,yb = self.xy(b)
            self.turn_on(xa,ya, xb,yb)
            return
        if cmd.startswith('turn off '):
            a,_,b = cmd.replace('turn off ','').partition(' through ')
            xa,ya = self.xy(a)
            xb,yb = self.xy(b)
            self.turn_off(xa,ya, xb,yb)
            return
        if cmd.startswith('toggle '):
            a,_,b = cmd.replace('toggle ','').partition(' through ')
            xa,ya = self.xy(a)
            xb,yb = self.xy(b)
            self.toggle(xa,ya, xb,yb)
            return
        print "Invalid cmd:",cmd
    

def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    l = LightsB()
    l.action(input)
    r = l.total_brightness()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print


# ========
#  Task B
# ========

# test cases
testcase('toggle 0,0 through 999,999', 2000000)
testcase('turn on 0,0 through 0,0', 1)

data = __file__.replace('b.py', '.input')
l = LightsB()
with open(data) as f:
    for line in f:
        if not line: continue
        l.action(line)
# 14110788
print 'Task B input file:',data,'Result:',l.total_brightness()
print

  