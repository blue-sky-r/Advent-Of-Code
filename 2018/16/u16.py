#!/usr/bin/env python

__motd__ = '--- Day 16: Chronal Classification ---'

__url__ = 'http://adventofcode.com/2018/day/16'


verbose = 0


class Cpu:

    def __init__(self):
        # mnemonic -> executable
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
        # code -> mnemonic (for task B only)
        self.instruction_code = {}
        # registers (for task B only)
        self.regs = [ 0 for i in range(4) ]

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
        regs[c] = regs[a] & b
        return regs

    def borr(self, regs, pars):
        """ rc <- ra | rb """
        i, a, b, c = pars
        regs[c] = regs[a] | regs[b]
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

    def input_effect(self, str):
        """ Before: [3, 2, 1, 1]
            9 2 1 2
            After:  [3, 2, 2, 1]
            returns True if we have complete set (before, code, after)
        """
        if str.startswith('Before: '):
            self.before = eval(str[len('Before: '):])
            self.expectcode = True
            return False
        if str.startswith('After: '):
            self.after = eval(str[len('After: '):])
            self.expectcode = False
            return True
        if self.expectcode:
            self.code = [ int(i) for i in str.split(' ') ]
        return False

    def input_code(self, str):
        """ execute single instruction on global cpu registers """
        code = [int(i) for i in str.split(' ')]
        instruction = self.instruction_code[code[0]]
        self.regs = self.instruction(instruction, self.regs[:], code)
        if verbose > 1: print "input_code(",str,") code:",code,"instructon:",instruction,"regs:",self.regs

    def input_line(self, str):
        """ build table and then exec code """
        # first build table
        if not self.instruction_code:
            # make guess if we have before=code-after triplets
            if self.input_effect(str):
                # guess
                match = self.find_ins(self.before, self.code, self.after)
                return match
        # then execute code
        else:
            self.input_code(str)

    def separator_detected(self, line, cnt=3):
        """ cnt empty lines """
        if line != '':
            self.empty_lines = 0
            return False
        self.empty_lines += 1
        return self.empty_lines >= cnt

    def task_a(self, input):
        """ task A """
        cnt = 0
        for line in input:
            match = self.input_line(line)
            if match and len(match) >= 3: cnt += 1
            if self.separator_detected(line): break
        return cnt

    def build_instruction_code(self, guesstab):
        """ settab code -> set_of_guesses"""
        # rectify instruction guess table
        while True:
            # items we are sure (guess has only 1 item)
            len1 = [code for code, guess in guesstab.items() if len(guess) == 1]
            # break if all instruction codes hae been identified
            if len(self.instruction_code) == len(guesstab):
                break
            # eliminate unique code from guesses
            for g1 in len1:
                item = list(guesstab[g1])[0]
                #
                for code, guess in guesstab.items():
                    if item not in guess: continue
                    if len(guess) == 1:
                        if code not in self.instruction_code:
                            # store code->mnemonic
                            self.instruction_code[code] = item
                            if verbose > 1: print "build_instruction_code() adding code:",code,"->",item
                    else:
                        guess.remove(item)
        return

    def task_b(self, input):
        """ task B """
        # build instruction table
        guesstab = {}
        for line in input:
            match = self.input_line(line)
            if match:
                # compose instructon table
                code = self.code[0]
                # keep only intersections
                guesstab[code] = guesstab[code].intersection(set(match)) if guesstab.get(code) else set(match)
            if self.separator_detected(line):
                # rectify instruction table before execution
                self.build_instruction_code(guesstab)
        #
        if verbose: print "task_b() regs:",self.regs
        # return just register[0]
        return self.regs[0]


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

# ========
#  Task B
# ========

# 706
testcase(Cpu(), None, 706, task_b=True)
