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
        return sm.get(2, 0) * sm.get(3, 0)

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

    def diff_match(self, id1, id2):
        """ retruns diff count and matching part """
        d, m = [], []
        for c1,c2 in zip(id1, id2):
            if c1 != c2:
                d.append(c1)
                continue
            m.append(c1)
        if verbose: print "diff_match(",id1,",",id2,") diff:", d," match:",m
        return len(d), m

    def find_min_diff_match(self):
        found = None
        for idx1,item1 in enumerate(self.id):
            id1 = item1.keys()[0]
            for idx2 in range(idx1+1, len(self.id)):
                item2 = self.id[idx2]
                id2 = item2.keys()[0]
                diff, match = self.diff_match(id1, id2)
                if found is None:
                    found = diff, ''.join(match)
                    continue
                if diff < found[0]:
                    found = diff, ''.join(match)
        return found

def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    i = IdScanner()
    r = i.id_lst(input)
    if task_b: r = i.find_min_diff_match()
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

# ========
#  Task B
# ========

# test cases
testcase(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz'], (1,'fgij'), task_b=True)

id = IdScanner()
with open(data) as f:
    for line in f:
        if not line: continue
        id.add_id(line.strip())
# (1, 'agimdjvlhedpsyoqfzuknpjwt')
print 'Task B input file:',data,'Result:',id.find_min_diff_match()
print
