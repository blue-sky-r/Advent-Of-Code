#!/usr/bin/env python

__motd__ = '--- Day 5: Doesn\'t He Have Intern-Elves For This? ---'

__url__ = 'http://adventofcode.com/2015/day/5'


verbose = 0


class Words:

    def three_vowels(self, s):
        cnt = 0
        for c in 'aeiou':
          cnt += s.count(c)
        return cnt >= 3

    def double(self, s):
        for i in range(ord('a'), ord('z')+1):
            if s.count("%s%s" % (chr(i),chr(i))) > 0: return True
        return False

    def ugly(self, s):
        ugl = ['ab', 'cd', 'pq', 'xy']
        for u in ugl:
            if s.count(u) > 0: return True
        return False

    def is_nice(self, s):
        return self.three_vowels(s) and self.double(s) and not self.ugly(s)
  


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
testcase('ugknbfddgicrmopn', True)
testcase('aaa',              True)
testcase('jchzalrnumimnmhp', False)
testcase('haegwjzuvuyypxyu', False)
testcase('dvszwmarrgswjxmb', False)

data = __file__.replace('a.py', '.input')
w = Words()
cnt = 0
with open(data) as f:
    for line in f:
        if not line: continue
        if w.is_nice(line): cnt += 1
# 238
print 'Task A input file:',data,'Result:',cnt
print
