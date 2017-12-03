#!/usr/bin/env python

__motd__ = '--- Day 2: Corruption Checksum ---'

__url__ = 'http://adventofcode.com/2017/day/2'


verbose = 0


class Checksum:

    def __init__(self):
        self.matrix = []
        
    def add_row(self, row):
        self.matrix.append(row)
        
    def add_row_str(self, str):
        row = [int(a) for a in str.strip().split()]
        self.add_row(row)
        
    def sum_maxmindiff(self):
        sum = 0
        for row in self.matrix:
            rmin,rmax = min(row),max(row)
            sum += rmax - rmin
            if verbose: print row,"min:",rmin,"max:",rmax,"sum:",sum
        return sum
                  
    def divisible(self, row):
        for i in row:
            for j in row:
                if i == j: continue
                if i % j == 0: return i,j
                
    def sum_divisible(self):
        sum = 0
        for row in self.matrix:
            a,b = self.divisible(row)
            sum += int(a / b)
            if verbose: print row,"a:",a,"b:",b,"sum:",sum
        return sum


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    c = Checksum()
    for r in input:
        c.add_row_str(r)
    r = c.sum_divisible() if task_b else c.sum_maxmindiff()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

data = [ '5 1 9 5', '7 5 3', '2 4 6 8']
testcase(data, 18)

data = __file__.replace('.py', '.input')
c = Checksum()
with open(data) as f:
    for line in f:
        c.add_row_str(line)

# 54426
print "task A:",c.sum_maxmindiff()

# ========
#  Task B
# ========

data = [ '5 9 2 8', '9 4 7 3', '3 8 6 5']
testcase(data, 9, task_b=True)

# 333
print "task B:",c.sum_divisible()

