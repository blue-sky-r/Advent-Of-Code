#!/usr/bin/env python

__motd__ = '--- Day 21: Scrambled Letters and Hash ---'

__url__ = 'http://adventofcode.com/2016/day/21'

verbose = 0

import re

class Scrambler:

    def __init__(self):
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
            'rotate based on position of letter (\w)':  self.unrot_r_pos_x,
            'reverse positions (\d+) through (\d+)':    self.rev_pos_x_y,
            'move position (\d+) to position (\d+)':    self.mov_pos_x_y
        }

    def integerize(self, v):
        """ return integer value of v (string or integer) """
        return v if type(v) == int else int(v)

    def swap_pos_x_y(self, str, sx, sy):
        """ swap position SX with position SY """
        x,y = self.integerize(sx), self.integerize(sy)
        l = list(str)
        l[x],l[y] = str[y],str[x]
        return ''.join(l)

    def swap_chr_x_y(self, str, cx, cy):
        """ swap letter CX with letter CY """
        return self.swap_pos_x_y(str, str.index(cx), str.index(cy))

    def rot_r_x(self, str, sx):
        """ rotate right SX steps """
        x = self.integerize(sx) % len(str)
        return str[-x:] + str[:-x]

    def rot_l_x(self, str, sx):
        """ rotate left SX steps """
        x = self.integerize(sx) % len(str)
        return str[x:] + str[:x]

    def rot_r_pos_x(self, str, cx):
        """ rotate based on position of letter CX """
        i = str.index(cx)
        if i>=4: i += 1
        i += 1
        return self.rot_r_x(str, i)

    def unrot_r_pos_x(self, str, cx):
        """ undo rotate based on position of letter CX """
        # try max 100
        for rotl in range(1, 100):
            src = self.rot_l_x(str, rotl)
            res = self.rot_r_pos_x(src, cx)
            if res == str:
                return src

    def rev_pos_x_y(self, str, sx, sy):
        """ reverse positions SX through SY """
        x,y = self.integerize(sx), self.integerize(sy)
        return str[:x] + ''.join(reversed(str[x:y+1])) + str[y+1:]

    def mov_pos_x_y(self, str, sx, sy):
        """ move position SX to position SY """
        x,y = self.integerize(sx), self.integerize(sy)
        l = list(str)
        del l[x]
        l.insert(y, str[x])
        return ''.join(l)

    def scramble(self, command, str):
        """ scramble str with command """
        if verbose: print '\t do:',command,'\t',str,'->',
        for regex,fnc in self.scramble_tab.items():
            m = re.match(regex, command)
            if m:
                par = list(m.groups())
                res = fnc(str, *par)
                if verbose: print res
                return res

    def unscramble(self, command, str):
        """ undo scramble str with command """
        if verbose: print '\t un:',command,'\t',str,'->',
        for regex,fnc in self.unscramble_tab.items():
            m = re.match(regex, command)
            if m:
                par = list(m.groups())
                if 'reverse' not in command: par.reverse()
                res = fnc(str, *par)
                if verbose: print res
                return res

    def scramble_file(self, str, fname):
        """ scramble str by program sequence """
        with open(fname) as f:
            for line in f:
                if not line.strip(): continue
                str = self.scramble(line.strip(), str)
        return str

    def unscramble_file(self, str, fname):
        """ undo scramble str by program sequence """
        with open(fname) as f:
            lines = f.read().splitlines()
        # process in reverse order
        lines.reverse()
        for line in lines:
            if not line.strip(): continue
            str = self.unscramble(line.strip(), str)
        return str


def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    if verbose: print
    password, program = input
    s = Scrambler()
    r = s.unscramble_file(password, program) if b else s.scramble_file(password, program)
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
s = Scrambler()
r = s.scramble_file(password, data)
# aefgbcdh
print 'Task A input file:',data,'Result:',r
print

# ========
#  Task B
# ========

# test cases
password = 'decab'
testcase((password, tcdata), 'abcde', b=True)

scrambled = 'fbgdceah'
s = Scrambler()
r = s.unscramble_file(scrambled, data)
# egcdahbf
print 'Task B input file:',data,'Result:',r
print
