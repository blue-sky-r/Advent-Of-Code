#!/usr/bin/env python

__motd__ = '--- Day 18: Like a Rogue ---'

__url__ = 'http://adventofcode.com/2016/day/18'

verbose = 0

class Tiles:

    def __init__(self, firstrow, symbols={'safe':'.', 'trap':'^'}):
        # init map
        self.map = [ firstrow ]
        # map symbols
        self.symbols = symbols

    def dump(self):
        " visualize map "
        return '\n'.join(self.map)

    def make_map(self, rows=10):
        " create map with rows $rows "
        while len(self.map) < rows:
            lastrow = self.map[len(self.map)-1]
            newrow  = ''.join(self.next_row(lastrow))
            self.map.append(newrow)
            if verbose: print; print self.dump(); print

    def next_row(self, row):
        " generate next row for map "
        return [ self.symbols['trap' if self.idx_is_trap(idx, row) else 'safe'] for idx,tile in enumerate(row) ]

    def idx_is_trap(self, idx, row):
        " apply rules for idx and return if it is a trap "
        # row with safe/no-trap sentinels
        sentrow = self.symbols['safe'] + row + self.symbols['safe']
        # adjust idx
        idx += 1
        # left-center-right map
        lcr = sentrow[idx-1:idx+2]
        # rules
        if lcr in ['^^.', '.^^', '^..', '..^']:
            return True
        return False

    def count_safe(self):
        " count all safe tiles on map "
        return sum([ row.count(self.symbols['safe']) for row in self.map ])

def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    row, cnt = input
    t = Tiles(row)
    t.make_map(cnt)
    r = t.count_safe()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
testcase(('..^^.', 3),           6 )
testcase(('.^^.^.^^^^', 10),    38 )

data = '^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^'
cnt  = 40
t = Tiles(data)
t.make_map(cnt)
r = t.count_safe()
# 1978
print 'Task A input:',data,'cnt:',cnt,'Result:',r
print

# ========
#  Task B
# ========

cnt = 400000
t.make_map(cnt)
r = t.count_safe()
# 20003246
print 'Task B input:',data,'cnt:',cnt,'Result:',r
print
