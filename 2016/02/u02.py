#!/usr/bin/env python

__url__ = 'http://adventofcode.com/2016/day/2'

verbose = 0

class Keypad:

    # sentinel char
    snt = '-'

    def __init__(self, layout, start_key='5'):
        self.key = start_key
        self.track = [start_key]
        self.layout = layout

    def locate(self, key):
        for r,row in enumerate(self.layout):
            if key in row:
                return r, row.index(key)

    def key_at(self, row, col):
        return self.layout[row][col]

    def next_key(self, dir):
        row,col = self.locate(self.key)
        if dir == 'U': return self.key_at(row-1, col)
        if dir == 'D': return self.key_at(row+1, col)
        if dir == 'L': return self.key_at(row, col-1)
        if dir == 'R': return self.key_at(row, col+1)
        # ignore unknown direction, so stay at current key
        return self.key

    def outside_limits(self, key):
        " we are outside limits if we are at sentinel key "
        return key == self.snt

    def ignore(self):
        " ignore movement outside keypad - we might sound an alarm here "
        pass

    def finger_move(self, dir):
        # next key
        key = self.next_key(dir)
        # track
        self.track.append(key)
        # check limits
        if self.outside_limits(key):
            self.ignore()
            return
        # valid move
        self.key = key

    def finger_sequence(self, seq):
        for m in seq:
            self.finger_move(m)
        return self.key

    def pin(self, rows):
        digit = []
        for row in rows:
            digit.append(self.finger_sequence(row))
        return ''.join(digit)

def testcase(input, result, layout):
    " testcase verifies if input returns result "
    print "TestCase",
    print "for input:",input,"\t expected result:",result,
    keys = Keypad(layout=layout)
    r = keys.pin(input)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    if verbose: print "Trace:",keys.track
    print

# ========
#  Task A
# ========

# use sentinel char around keypad
#
layoutA = [
    '-----',
    '-123-',
    '-456-',
    '-789-',
    '-----'
]

# test cases
testcase(['ULL','RRDDD','LURDL','UUUUD'], '1985', layoutA)

data = __file__.replace('.py', '.input')
keys = Keypad(layout=layoutA)
with open(data) as f:
    rows = []
    for line in f:
        if not line: continue
        rows.append(line)
    pin = keys.pin(rows)
# 18843
print 'Task A input file:',data,'Result:',pin
if verbose: print "Trace:",keys.track
print

# ========
#  Task B
# ========

# use sentinel char around keypad
#
layoutB = [
    '-------',
    '---1---',
    '--234--',
    '-56789-',
    '--ABC--',
    '---D---',
    '-------'
]

# test cases
testcase(['ULL','RRDDD','LURDL','UUUUD'], '5DB3', layoutB)

keys  = Keypad(layout=layoutB)
with open(data) as f:
    rows = []
    for line in f:
        if not line: continue
        rows.append(line)
    pin = keys.pin(rows)
# 67BB9
print 'Task B input file:',data,'Result:',pin
if verbose: print "Trace:",keys.track
