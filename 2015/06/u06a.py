#!/usr/bin/env python

__motd__ = '--- Day 6: Probably a Fire Hazard ---'

__url__ = 'http://adventofcode.com/2015/day/6'


verbose = 0


class LightsA:

    def __init__(self, x=1000, y=1000, state=0):
        self.grid = []
        for i in range(x):
            self.grid.append([state for i in range(y)])
      
    def on(self, x,y):
        self.grid[x][y] = 1
    
    def off(self, x,y):
        self.grid[x][y] = 0
    
    def toggleXY(self, x,y):
        self.grid[x][y] = 0 if self.grid[x][y] == 1 else 1
    
    def lit_cnt(self):
        sum = 0
        for x in range(1000):
            sum += self.grid[x].count(1)
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
    l = LightsA()
    l.action(input)
    r = l.lit_cnt()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print


# ========
#  Task A
# ========

# test cases
testcase('turn on 0,0 through 999,999', 1000000)
testcase('toggle 0,0 through 999,0', 1000)
testcase('turn off 499,499 through 500,500', 0)

data = __file__.replace('a.py', '.input')
l = LightsA()
with open(data) as f:
    for line in f:
        if not line: continue
        l.action(line)
# 377891
print 'Task A input file:',data,'Result:',l.lit_cnt()
print


