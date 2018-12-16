#!/usr/bin/env python

__motd__ = '--- Day 16: Chronal Classification ---'

__url__ = 'http://adventofcode.com/2018/day/16'


verbose = 0


class Cpu:

    def __init__(self):
        self.instruction_set = {
            # ADD
            'addr': self.addr,
            'addi': self.addi,
            # MULT
            'mulr': self.mulr,
            'muli': self.muli,
            # AND
            'banr': self.banr,
            'bani': self.bani,
            # OR
            'borr': self.borr,
            'bori': self.bori,
            # SET
            'setr': self.setr,
            'seti': self.seti,
            # >
            'gtir': self.gtir,
            'gtri': self.gtri,
            'gtrr': self.gtrr,
            # =
            'eqir': self.eqir,
            'eqri': self.eqri,
            'eqrr': self.eqrr
        }

    def instruction(self, code, regs, pars):
        """ execute single instruction on registers input """
        return self.instruction_set[code](regs, pars)

    def addr(self, regs, pars):
        """ rc <- ra + rb """
        i, a, b, c = pars
        regs[c] = regs[a] + regs[b]
        return regs

    def addi(self, regs, pars):
        """ rc <- ra + #b """
        i, a, b, c = pars
        regs[c] = regs[a] + b
        return regs

    def mulr(self, regs, pars):
        """ rc <- ra * rb """
        i, a, b, c = pars
        regs[c] = regs[a] * regs[b]
        return regs

    def muli(self, regs, pars):
        """ rc <- ra * #b """
        i, a, b, c = pars
        regs[c] = regs[a] * b
        return regs

    def banr(self, regs, pars):
        """ rc <- ra & rb """
        i, a, b, c = pars
        regs[c] = regs[a] & regs[b]
        return regs

    def bani(self, regs, pars):
        """ rc <- ra & #b """
        i, a, b, c = pars
        regs[c] = regs[a] | b
        return regs

    def borr(self, regs, pars):
        """ rc <- ra | rb """
        i, a, b, c = pars
        regs[c] = regs[a] & regs[b]
        return regs

    def bori(self, regs, pars):
        """ rc <- ra | #b """
        i, a, b, c = pars
        regs[c] = regs[a] | b
        return regs

    def setr(self, regs, pars):
        """ rc <- ra """
        i, a, b, c = pars
        regs[c] = regs[a]
        return regs

    def seti(self, regs, pars):
        """ rc <- #a """
        i, a, b, c = pars
        regs[c] = a
        return regs

    def gtir(self, regs, pars):
        """ rc <- 1 if #a > rb """
        i, a, b, c = pars
        regs[c] = 1 if a > regs[b] else 0
        return regs

    def gtri(self, regs, pars):
        """ rc <- 1 if ra > #b """
        i, a, b, c = pars
        regs[c] = 1 if regs[a] > b else 0
        return regs

    def gtrr(self, regs, pars):
        """ rc <- 1 if ra > rb """
        i, a, b, c = pars
        regs[c] = 1 if regs[a] > regs[b] else 0
        return regs

    def eqir(self, regs, pars):
        """ rc <- 1 if #a = rb """
        i, a, b, c = pars
        regs[c] = 1 if a == regs[b] else 0
        return regs

    def eqri(self, regs, pars):
        """ rc <- 1 if ra = #b """
        i, a, b, c = pars
        regs[c] = 1 if regs[a] == b else 0
        return regs

    def eqrr(self, regs, pars):
        """ rc <- 1 if ra = rb """
        i, a, b, c = pars
        regs[c] = 1 if regs[a] == regs[b] else 0
        return regs

    def find_ins(self, regsin, pars, regsout):
        """ find instructions matching input/output """
        match = []
        for code,ins in self.instruction_set.items():
            rregs = self.instruction(code, regsin[:], pars)
            if verbose > 2: print "find_ins(regsin:",regsin,"pars:",pars,"regsout:",regsout,") code:",code,"rregs:",rregs
            if rregs == regsout:
                match.append(code)
        if verbose > 1: print "find_ins(regsin:",regsin,"pars:",pars,"regsout:",regsout,") match:",match
        return match

    def input_line(self, str):
        """ Before: [3, 2, 1, 1]
            9 2 1 2
            After:  [3, 2, 2, 1]  """
        if str.startswith('Before: '):
            self.before = eval(str[len('Before: '):])
            return False
        if str.startswith('After: '):
            self.after = eval(str[len('After: '):])
            return True
        self.code = [ int(i) for i in str.split(' ') ]
        return False

    def task_a(self, input):
        """ task A """
        cnt = 0
        # count empty (separator) lines
        sepline = 0
        for line in input:
            # is empty ?
            if line == '':
                sepline += 1
                # 3 empty lines are separator for task B
                if sepline >= 3: break
            else:
                sepline = 0
                if self.input_line(line):
                    # guess
                    match = self.find_ins(self.before, self.code, self.after)
                    # count only with 3 or more opcodes
                    if len(match) >= 3: cnt += 1
        return cnt

    def task_b(self, input):
        """ task B """
        return


def testcase(sut, input, result, task_b=False):
    " testcase verifies if input returns result "
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [line.rstrip() for line in f]
    #
    print "TestCase", "B" if task_b else "A", "for input:", data if 'data' in vars() else input, "\t expected result:", result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    #r = f.find_duplo(input) if task_b else f.change_seq(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========

data = """
Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]
"""
# test cases
testcase(Cpu(), data.strip().split('\n'),          1)

# 651
testcase(Cpu(), None, 651)
xxx
# ========
#  Task B
# ========

# test cases
testcase((), ['', '', '', ''],            2, task_b=True)

# [1m 34s] 56360
testcase((), None, 2, task_b=True)
