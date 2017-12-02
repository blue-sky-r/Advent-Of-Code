#!/usr/bin/env python

__motd__ = '--- Day 1: Inverse Captcha ---'

__url__ = 'http://adventofcode.com/2017/day/1'


verbose = 0


class Captcha:

    def __init__(self):
        self.sum = 0

    def sum_seq(self, str, offset=1):
        for idx1,c1 in enumerate(str):
            idx2 = (idx1+offset) % len(str)
            c2   = str[idx2]
            if verbose: print "idx1:",idx1,"c1:",c1,"idx2:",idx2,"c2:",c2,"sum:",self.sum
            if c1 == c2: self.sum += int(c1)
        return self.sum
          
    def sum_half(self, str):
        return self.sum_seq(str, offset=len(str)/2)


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    c = Captcha()
    r = c.sum_half(input) if task_b else c.sum_seq(input)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
testcase('1122',     3)
testcase('1111',     4)
testcase('1234',     0)
testcase('91212129', 9)

data = __file__.replace('.py', '.input')
c = Captcha()
with open(data) as f:
    for line in f:
        if not line: continue
        c.sum_seq(line.strip())
# 1203
print 'Task A input file:',data,'Result:',c.sum
print

# ========
#  Task A
# ========

# test cases
testcase('1212',     6, task_b=True)
testcase('1221',     0, task_b=True)
testcase('123123',  12, task_b=True)
testcase('12131415', 4, task_b=True)

c = Captcha()
with open(data) as f:
    for line in f:
        if not line: continue
        c.sum_half(line.strip())
# 1146
print 'Task B input file:',data,'Result:',c.sum
print
