#!/usr/bin/env python

__motd__ = '--- Day 2: 1202 Program Alarm ---'

__url__ = 'http://adventofcode.com/2019/day/2'


verbose = 0


class Computer:

    def __init__(self):
        self.program = None
        self.asm = {
             1: self.asm_add,
             2: self.asm_mult,
            99: self.asm_halt
        }

    def asm_halt(self):
        """ halt the computer """
        if verbose > 2: print 'DBG: HALT @',self.pc
        self.running = False
        return self

    def asm_add(self):
        """ add @1 + @2 -> @3 """
        a, b, c = self.program[self.pc+1], self.program[self.pc+2], self.program[self.pc+3]
        if verbose > 2: print 'DBG: ADD @%d + @%d -> @%d' % (a,b,c)
        self.program[c] = self.program[a] + self.program[b]
        self.pc += 4
        return self

    def asm_mult(self):
        """ mul @1 * @2 -> @3 """
        a, b, c = self.program[self.pc + 1], self.program[self.pc + 2], self.program[self.pc + 3]
        if verbose > 2: print 'DBG: MUL @%d * @%d -> @%d' % (a, b, c)
        self.program[c] = self.program[a] * self.program[b]
        self.pc += 4
        return self

    def step(self):
        """ execute one step at pc """
        asm = self.program[self.pc]
        if verbose > 3: print 'DBG: executing code:', asm,'@',self.pc
        asm_fnc = self.asm[asm]
        return asm_fnc()

    def program_alarm(self, codestr):
        """ restore gravity assist """
        at1, at2 = codestr[-4:-2], codestr[-2:]
        self.program[1], self.program[2] = int(at1), int(at2)
        return self

    def program_load(self, prog):
        """ load csv string format to list """
        self.program = [int(i) for i in prog.split(',')]
        self.pc = 0
        self.running = False
        return self

    def run_prog(self, prog, alarm=None):
        """ execute program prog """
        self.program_load(prog)
        if alarm: self.program_alarm(alarm)
        self.running = True
        while self.running:
            self.step()

    def task_a(self, input, alarm=None):
        """ task A """
        self.run_prog(input, alarm)
        return self.program[0]

    def task_b(self, input, find):
        """ task B """
        for nv in range(10000):
            result = self.task_a(input, alarm='%04d' % nv)
            if verbose: print 'DBG: nv=%d result=%d' % (nv, result)
            if result == find: return nv
        return


def testcase(sut, input, result, alarm=None, task_b=False):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = f.readline().strip()
    #
    #
    print "TestCase", "B" if task_b else "A",
    print "for input:", data if 'data' in vars() else input,
    print "\t expected result:", result,
    r = sut.task_a(input, alarm) if not task_b else sut.task_b(input, find=alarm)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    if verbose > 1: print 'Dump:',sut.program
    print

# ========
#  Task A
# ========

# test cases
testcase(Computer(), '1,9,10,3,2,3,11,0,99,30,40,50', 3500)
testcase(Computer(), '1,0,0,0,99', 2)
testcase(Computer(), '2,3,0,3,99', 2)
testcase(Computer(), '2,4,4,5,99,0', 2)
testcase(Computer(), '1,1,1,4,99,5,6,0,99', 30)

# 2842648
testcase(Computer(),  None,  2842648, '1202')

# ========
#  Task b
# ========

# test cases
testcase(Computer(), None, 1202, 2842648, task_b=True)

# 9074
testcase(Computer(), None, 9074, 19690720, task_b=True)
