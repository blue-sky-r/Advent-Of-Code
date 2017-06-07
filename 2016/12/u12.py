#!/usr/bin/env python

__motd__ = "--- Day 12: Leonardo's Monorail ---"

__url__ = 'http://adventofcode.com/2016/day/12'

verbose = 0

import re

class Assembunny:

    def __init__(self):
        self.reg = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0
        }
        self.pc = 0
        self.parse_ins = {
            'cpy\s+(\w+)\s+(\w)':   self.cpy_x_y,
            'inc\s+(\w)':           self.inc_x,
            'dec\s+(\w)':           self.dec_x,
            'jnz\s+(\w)\s+(-?\w+)': self.jnz_x_y,
        }

    def dump(self, ins):
        return '\t'.join([ "%10s" % ins, "PC:%03d" % (self.pc) ] + [ "%s:%03d" % (r.upper(), self.reg[r]) for r in sorted(self.reg.keys()) ])

    def is_reg(self,x):
        return x in self.reg

    def cpy_x_y(self, x, y):
        self.reg[y] = self.reg[x] if self.is_reg(x) else int(x)

    def inc_x(self, x):
        self.reg[x] += 1

    def dec_x(self, x):
        self.reg[x] -= 1

    def jnz_x_y(self, x, y):
        if self.is_reg(x):
            if self.get_reg(x) != 0:
                self.pc += int(y) - 1
        else:
            if int(x) != 0:
                self.pc += int(y) - 1

    def get_reg(self, r):
        return self.reg[r]

    def set_reg(self, r, val):
        self.reg[r] = int(val)

    def exec_ins(self, ins):
        for mask,fnc in self.parse_ins.items():
            m = re.match(mask, ins)
            if not m: continue
            if len(m.groups()) == 1:
                fnc(m.group(1))
                break
            if len(m.groups()) == 2:
                fnc(m.group(1), m.group(2))
                break
        self.pc += 1
        if verbose: print self.dump(ins)

    def exec_program(self, prog):
        if verbose: print
        self.pc = 0
        while self.pc < len(prog):
            self.exec_ins(prog[self.pc])
        if verbose: print self.dump('-')

    def exec_file(self, fname):
        with open(fname) as f:
            program = f.read().splitlines()
            self.exec_program(program)


def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input file:",input,"\t expected result:",result,
    ab = Assembunny()
    ab.exec_program(input)
    r = ab.get_reg('a')
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    if verbose: print "Trace:",
    print

# ========
#  Task A
# ========

# test cases
prog = ['cpy 41 a','inc a','inc a','dec a','jnz a 2','dec a']
testcase(prog, 42)

data = __file__.replace('.py', '.input')
ab = Assembunny()
ab.exec_file(data)
r = ab.get_reg('a')
# 318020
print 'Task A input file:',data,'Result:',r
print

# ========
#  Task B
# ========

ab = Assembunny()
ab.set_reg('c', 1)
ab.exec_file(data)
r = ab.get_reg('a')
# 9227674
print 'Task B input file:',data,'Result:',r
print
