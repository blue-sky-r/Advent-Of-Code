#!/usr/bin/env python

__motd__ = '--- Day 1: I Was Told There Would Be No Math ---'

__url__ = 'http://adventofcode.com/2015/day/2'


def ribbon_area(dim):
    l,w,h = map(int, dim.split('x'))
    # paper
    area = [ l*w, l*h, w*h ]
    plus = min(area)
    # ribbon
    perim = [ 2*l+2*w, 2*l+2*h, 2*w+2*h ]
    bow   = l*w*h
    #
    return plus + 2*sum(area), bow + min(perim)


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    a,b = ribbon_area(input)
    r = b if task_b else a
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print


# ========
#  Task A
# ========

# test cases
testcase('2x3x4',  58)
testcase('1x1x10', 43)

data = __file__.replace('.py', '.input')
total = (0,0)
with open(data) as f:
    for line in f:
        if not line: continue
        a,b = ribbon_area(line.strip())
        total = total[0]+a, total[1]+b
# 1606483
print 'Task A input file:',data,'Result:',total[0]
print

# ========
#  Task B
# ========

testcase('2x3x4',  34, task_b=True)
testcase('1x1x10', 14, task_b=True)

# 3842356
print 'Task B input file:',data,'Result:',total[1]
print
