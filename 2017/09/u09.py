#!/usr/bin/env python

__motd__ = '--- Day 9: Stream Processing ---'

__url__ = 'http://adventofcode.com/2017/day/9'


verbose = 0


class Stream:

    def __init__(self):
        pass

    def process(self, data):
        # G-arbage, D-ata
        state = ''
        ignore, garbage = False, False
        score, level, gcnt = 0, 0, 0
        for c in data:
            if verbose: print 'c:',c,'garbage:',garbage,'ignore:',ignore,'level:',level,'score:',score
            if ignore:
                ignore = False
                continue
            if not garbage and c == '<':
                garbage = True
                continue
            if garbage and c == '!':
                ignore = True
                continue
            if garbage and c == '>':
                garbage = False
                continue
            if garbage:
                gcnt += 1
            if not garbage and c == '{':
                level  += 1
                score  += level
            if not garbage and c == '}':
                level -= 1
        return score, gcnt


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    s = Stream()
    ra, rb = s.process(input)
    r = rb if task_b else ra
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

testcase('{}',               1)
testcase('{{{}}}',           6)
testcase('{{},{}}',          5)
testcase('{{{},{},{{}}}}',  16)
testcase('{<a>,<a>,<a>,<a>}', 1)
testcase('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9)
testcase('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9)
testcase('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3)

data = __file__.replace('.py', '.input')
s = Stream()
cnta, cntb = 0, 0
with open(data) as f:
    for line in f:
        ra, rb = s.process(line)
        cnta += ra
        cntb += rb
# 17390
print 'Task A input file:',data,'Result:',cnta

# ========
#  Task A
# ========

testcase('<>',                   0, task_b=True)
testcase('<random characters>', 17, task_b=True)
testcase('<<<<>',                3, task_b=True)
testcase('<{!>}>',               2, task_b=True)
testcase('<!!>',                 0, task_b=True)
testcase('<!!!>>',               0, task_b=True)
testcase('<{o"i!a,<{i<a>',      10, task_b=True)

# 7825
print 'Task A input file:',data,'Result:',cntb
    