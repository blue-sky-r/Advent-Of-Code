#!/usr/bin/env python

__motd__ = '--- Day 3: No Matter How You Slice It ---'

__url__ = 'http://adventofcode.com/2018/day/3'


verbose = 1


class Fabric:

    def __init__(self, size=1000):
        self.size = size
        self.xy = {}
        for x in range(size):
            for y in range(size):
                self.xy[x,y] = []

    def show(self):
        for y in range(self.size):
            for x in range(self.size):
                l = len(self.xy[x,y])
                print l if l > 0 else ".",
            print
        print
        return

    def claim(self, id, x,y, wide, tall):
        for xx in range(x, x+wide):
            for yy in range(y, y+tall):
                self.xy[xx,yy].append(id)

    def count_overlap(self, threshold=2):
        cnt = 0
        for x in range(self.size):
            for y in range(self.size):
                if len(self.xy[x,y]) >= threshold:
                    cnt += 1
        return cnt

    def claim_str(self, str):
        """ parse string format: #133 @ 468,238: 10x14 """
        id,at,xy,wxt = str.split(' ')
        id = int(id.strip('#'))
        x,y = xy.split(',')
        x,y = int(x), int(y.strip(':'))
        w,t = wxt.split('x')
        w,t = int(w), int(t)
        if verbose: print "claim_str(",str,") -> id:",id,", x:",x,", y:",y,", w:",w,", t:",t
        return id, x,y, w, t

    def parse_str(self, str):
        """ """
        id, x,y, w,t = self.claim_str(str)
        self.claim(id, x,y, w,t)
        return

    def parse_lst(self, lst):
        """ """
        for s in lst:
            self.parse_str(s)
            if verbose: self.show()
        return


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    f = Fabric(size=10)
    f.parse_lst(input)
    r = f.count_overlap() if task_b else f.count_overlap()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
testcase(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'], 4)

data = __file__.replace('.py', '.input')
fa = Fabric()
with open(data) as f:
    for line in f:
        if not line: continue
        fa.parse_str(line.strip())
# 112418
print 'Task A input file:',data,'Result:',fa.count_overlap()
print

# ========
#  Task B
# ========

