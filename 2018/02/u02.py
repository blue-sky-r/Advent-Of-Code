#!/usr/bin/env python

__motd__ = '--- Day 2: Inventory Management System ---'

__url__ = 'http://adventofcode.com/2018/day/2'


verbose = 0


class IdScanner:

    def __init__(self):
        self.id = []

    def chr_count(self, str):
        cnt = {}
        for c in str:
            if c in cnt: continue
            cnt[c] = str.count(c)
        if verbose: print "chr_count(",str,") ->",cnt
        return cnt

    def checksum(self):
        sm = {}
        for item in self.id:
            id = item.keys()[0]
            for chrcnt, times in item[id].items():
                sm[chrcnt] = sm.get(chrcnt, 0) + 1
        return sm[2] * sm[3]

    def id_counts(self, str):
        """ get counts for id str """
        counts = {}
        for char,cnt in self.chr_count(str).items():
            counts[cnt] = counts.get(cnt, 0) + 1
        if verbose: print "id_counts(",str,") counts:",counts
        return counts

    def add_id(self, str):
        item = {
            str: self.id_counts(str)
        }
        self.id.append(item)
        return item

    def id_lst(self, lst):
        for id in lst:
            self.add_id(id)
        return self.checksum()


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    i = IdScanner()
    r = i.id_lst(input) if task_b else i.id_lst(input)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
testcase(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'], 12)

data = __file__.replace('.py', '.input')
id = IdScanner()
with open(data) as f:
    for line in f:
        if not line: continue
        id.add_id(line.strip())
# 5434
print 'Task A input file:',data,'Result:',id.checksum()
print
xxx
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
