#!/usr/bin/env python

__motd__ = '--- Day 1: Chronal Calibration ---'

__url__ = 'http://adventofcode.com/2018/day/1'


verbose = 0


class Frequency:

    def __init__(self, start=0):
        self.f = start
        self.history = [self.f]

    def change_seq(self, lst):
        self.f += sum(lst)
        return self.f

    def change_str(self, str):
        self.f += int(str)
        return self.f

    def change_check_duplo(self, str):
        f = self.change_str(str)
        if f in self.history:
            return f
        self.history.append(f)

    def find_duplo(self, lst):
        while True:
            for f in lst:
                dupl = self.change_check_duplo(f)
                if dupl is not None: return dupl


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    f = Frequency()
    r = f.find_duplo(input) if task_b else f.change_seq(input)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
testcase([+1, -2, +3, +1], 3)
testcase([+1, +1, +1],     3)
testcase([+1, +1, -2],     0)
testcase([-1, -2, -3],    -6)

data = __file__.replace('.py', '.input')
fq = Frequency()
with open(data) as f:
    for line in f:
        if not line: continue
        fq.change_str(line.strip())
# 411
print 'Task A input file:',data,'Result:',fq.f
print

# ========
#  Task B
# ========

# test cases
testcase([+1, -2, +3, +1],          2, task_b=True)
testcase([+1, -1],                  0, task_b=True)
testcase([+3, +3, +4, -2, -4],     10, task_b=True)
testcase([-6, +3, +8, +5, -6],      5, task_b=True)
testcase([+7, +7, -2, -7, -4],     14, task_b=True)

fq = Frequency()
dupl = None
while dupl is None:
    if verbose: print "history size:",len(fq.history)
    with open(data) as f:
        for line in f:
            if not line: continue
            dupl = fq.change_check_duplo(line.strip())
            if dupl is not None: break
# [1m 34s] 56360
print 'Task B input file:',data,'Result:',dupl
print
