#!/usr/bin/env python

__motd__ = '--- Day 2: 1202 Program Alarm ---'

__url__ = 'http://adventofcode.com/2019/day/2'


verbose = 0


class Computer:

    def __init__(self):
        self.pc = 0
        self.program = None
        self.running = False
        self.asm = {
             1: self.asm_add,
             2: self.asm_mult,
            99: self.asm_halt
        }

    def asm_halt(self):
        """ halt the computer """
        if verbose: print 'DBG: HALT @',self.pc
        self.running = False
        return self

    def asm_add(self):
        """ add @1 + @2 -> @3 """
        a, b, c = self.program[self.pc+1], self.program[self.pc+2], self.program[self.pc+3]
        if verbose: print 'DBG: ADD @%d + @%d -> @%d' % (a,b,c)
        self.program[c] = self.program[a] + self.program[b]
        self.pc += 4
        return self

    def asm_mult(self):
        """ mul @1 * @2 -> @3 """
        a, b, c = self.program[self.pc + 1], self.program[self.pc + 2], self.program[self.pc + 3]
        if verbose: print 'DBG: MUL @%d * @%d -> @%d' % (a, b, c)
        self.program[c] = self.program[a] * self.program[b]
        self.pc += 4
        return self

    def step(self):
        """ execute one step at pc """
        asm = self.program[self.pc]
        if verbose: print 'DBG: executing code:', asm,'@',self.pc
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

    def task_b(self, input):
        """ task B """
        return


def testcase(sut, input, result, task_b=False):
    """ testcase verifies if input returns result """
    alarm = None
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = f.readline().strip()
        alarm = '1202'
    #
    #
    print "TestCase", "B" if task_b else "A",
    print "for input:", data if 'data' in vars() else input,
    print "\t expected result:", result,
    r = sut.task_a(input, alarm) if not task_b else sut.task_b(input)
    #r = f.find_duplo(input) if task_b else f.change_seq(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print 'Dump:',sut.program
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
testcase(Computer(),  None,  2842648)
