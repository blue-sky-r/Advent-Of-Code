#!/usr/bin/env python

__motd__ = '--- Day 10: Knot Hash ---'

__url__ = 'http://adventofcode.com/2017/day/10'


verbose = 0


class Knot:

    def __init__(self, size=256):
        self.size = size
        self.circle = [ x for x in range(size) ]
        self.cpos = 0
        self.skip = 0

    def visualize(self, len=0):
        str = []
        for idx, c in enumerate(self.circle):
            if len == 1 and idx == self.cpos:
                str.append('([%d])' % c)
                continue
            if idx == self.cpos:
                str.append('([%d]' % c)
                continue
            if idx == (self.cpos+len-1) % self.size:
                str.append('%d)' % c)
                continue
            str.append('%d' % c)
        return ' '.join(str)

    def signature(self):
        return self.circle[0] * self.circle[1]

    def instructions(self, str):
        for ins in [ int(x) for x in str.split(',') ]:
            if verbose:
                print
                print "len:",ins,"cpos:",self.cpos,"skip:",self.skip,"\t\t",self.visualize(ins)
            self.step(ins)
        if verbose:
            print
            print "len:", ins, "cpos:", self.cpos, "skip:", self.skip, "\t\t", self.visualize(ins)
        return self.signature()

    def step(self, len):
        self.reverse_len(len)
        self.cpos = (self.cpos + len + self.skip) % self.size
        self.skip += 1

    def reverse_len(self, len):
        # part to reverse
        rev = []
        for idx in range(len):
            rev.append(self.circle[(self.cpos+idx)%self.size])
        # reverse
        rev = rev[::-1]
        # replace
        for idx in range(len):
            self.circle[(self.cpos+idx)%self.size] = rev[idx]
            

def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    k = Knot(5)
    r = k.instructions(input)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

testcase('3,4,1,5', 12)

data = __file__.replace('.py', '.input')
k = Knot()
with open(data) as f:
    for line in f:
        r = k.instructions(line)
# 38628
print 'Task A input file:',data,'Result:',r
