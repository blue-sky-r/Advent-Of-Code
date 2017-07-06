#!/usr/bin/env python

__motd__ = '--- Day 21: Scrambled Letters and Hash ---'

__url__ = 'http://adventofcode.com/2016/day/21'

verbose = 1

import re

class Scrambler:

    def __init__(self, str):
        self.str = str
        self.scramble_tab = {
            'swap position (\d+) with position (\d+)':  self.swap_pos_x_y,
            'swap letter (\w) with letter (\w)':        self.swap_chr_x_y,
            'rotate right (\d+) steps?':                self.rot_r_x,
            'rotate left (\d+) steps?':                 self.rot_l_x,
            'rotate based on position of letter (\w)':  self.rot_r_pos_x,
            'reverse positions (\d+) through (\d+)':    self.rev_pos_x_y,
            'move position (\d+) to position (\d+)':    self.mov_pos_x_y
        }
        self.unscramble_tab = {
            'swap position (\d+) with position (\d+)':  self.swap_pos_x_y,
            'swap letter (\w) with letter (\w)':        self.swap_chr_x_y,
            'rotate right (\d+) steps?':                self.rot_l_x,
            'rotate left (\d+) steps?':                 self.rot_r_x,
            'rotate based on position of letter (\w)':  self.rot_l_pos_x,
            'reverse positions (\d+) through (\d+)':    self.rev_pos_x_y,
            'move position (\d+) to position (\d+)':    self.mov_pos_x_y
        }

    def swap_pos_x_y(self, x, y):
        l = list(self.str)
        l[x] = self.str[y]
        l[y] = self.str[x]
        self.str = ''.join(l)

    def swap_chr_x_y(self, x, y):
        self.swap_pos_x_y(self.str.index(x), self.str.index(y))

    def rot_r_x(self, x):
        x = x % len(self.str)
        self.str = self.str[-x:] + self.str[:-x]

    def rot_l_x(self, x):
        x = x % len(self.str)
        self.str = self.str[x:] + self.str[:x]

    def rot_r_pos_x(self, x):
        i = self.str.index(x)
        if i>=4: i += 1
        i += 1
        self.rot_r_x(i)

    def rot_l_pos_x(self, x):
        i = self.str.index(x)
        if i>=4: i += 1
        i += 1
        self.rot_l_x(i)

    def rev_pos_x_y(self, x, y):
        self.str = self.str[:x] + ''.join(reversed(self.str[x:y+1])) + self.str[y+1:]

    def mov_pos_x_y(self, x, y):
        l = list(self.str)
        del l[x]
        l.insert(y, self.str[x])
        self.str = ''.join(l)

    def scramble(self, command):
        if verbose: print command,'\t',self.str,'->',
        for regex,fnc in self.scramble_tab.items():
            m = re.match(regex, command)
            if m:
                par = [ p if 'letter' in regex else int(p) for p in m.groups() ].reverse()
                fnc(*par)
                if verbose: print self.str
                return True

    def unscramble(self, command):
        if verbose: print command,'\t',self.str,'->',
        for regex,fnc in self.unscramble_tab.items():
            m = re.match(regex, command)
            if m:
                par = [ p if 'letter' in regex else int(p) for p in m.groups() ]
                fnc(*par)
                if verbose: print self.str
                return True

    def exec_file(self, fname):
        with open(fname) as f:
            for line in f:
                if not line.strip(): continue
                if not self.scramble(line.strip()):
                    print "CMD error:",line
        return self.str


def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    password, program = input
    s = Scrambler(password)
    r = s.exec_file(program)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
tcdata = __file__.replace('.py', '.tc.input')
password = 'abcde'
testcase((password, tcdata), 'decab')

data = __file__.replace('.py', '.input')
password = 'abcdefgh'
s = Scrambler(password)
r = s.exec_file(data)
# aefgbcdh
print 'Task A input file:',data,'Result:',r
print
xxx
# ========
#  Task B
# ========

# test cases
testcase('', 0, b=True)

with open(data) as f:
    for line in f:
        if not line: continue

#
print 'Task B input file:',data,'Result:',
if verbose: print "Trace:",
