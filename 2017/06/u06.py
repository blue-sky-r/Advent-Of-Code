#!/usr/bin/env python

__motd__ = '--- Day 6: Memory Reallocation ---'

__url__ = 'http://adventofcode.com/2017/day/6'


verbose = 0


class Realloc:

    def __init__(self):
        self.history = []

    def balancing_str(self, str):
        return self.balancing([ int(x) for x in str.split() ])

    def balancing(self, state):
        steps = 0
        while state not in self.history:
            self.history.append(state)
            idx = self.max_idx(state)
            state = self.balance_idx(state, idx)
            if verbose: print "idx:",idx,"state:",state
            steps += 1
        return steps,len(self.history) - self.history.index(state)

    def max_idx(self, state):
        m = max(state)
        return state.index(m)

    def balance_idx(self, state, idx):
        balanced = state[:]
        val = balanced[idx]
        balanced[idx] = 0
        while val>0:
            idx = (idx+1) % len(balanced)
            balanced[idx] += 1
            val -= 1
        return balanced


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    m = Realloc()
    steps,loop = m.balancing_str(input)
    r = loop if task_b else steps
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

testcase('0 2 7 0',  5)

data = __file__.replace('.py', '.input')
m = Realloc()
with open(data) as f:
    for line in f:
        if not line: continue
        a,b = m.balancing_str(line)
# 6681
print 'Task A input file:',data,'Result:',a
print

# ========
#  Task B
# ========

testcase('0 2 7 0',  4, task_b=True)

# 2392
print 'Task B input file:',data,'Result:',b
print
