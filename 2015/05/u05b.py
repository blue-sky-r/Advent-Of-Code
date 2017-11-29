#!/usr/bin/env python

__motd__ = '--- Day 5: Doesn\'t He Have Intern-Elves For This? ---'

__url__ = 'http://adventofcode.com/2015/day/5'


verbose = 0


class Words:

    def has_pairs(self, s, n=2):
        for i in range(len(s)-1):
            pair = s[i:i+2]
            cnt = s.count(pair)
            if cnt >= n: return True
        return False

    def has_triplet(self, s):
        for i in range(len(s)-2):
            triplet = s[i:i+3]
            if triplet.endswith(triplet[0]): return True
        return False

    def is_nice(self, s):
        return self.has_pairs(s) and self.has_triplet(s)


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    w = Words()
    r = w.is_nice(input)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print


# ========
#  Task A
# ========

# test cases
testcase('qjhvhtzxzqqjkmpb', True)
testcase('xxyxx', True)
testcase('uurcxstgmygtbstg', False)
testcase('ieodomkazucvgmuy', False)

data = __file__.replace('b.py', '.input')
w = Words()
cnt = 0
with open(data) as f:
    for line in f:
        if not line: continue
        if w.is_nice(line): cnt += 1
# 69
print 'Task B input file:',data,'Result:',cnt
print
