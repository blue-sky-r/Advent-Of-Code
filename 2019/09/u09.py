#!/usr/bin/env python

__motd__ = '--- Day 9: Sensor Boost ---'

__url__ = 'http://adventofcode.com/2019/day/9'

import math

verbose = 0


class Computer3:
    """ taken from unit 05 - changes:
    - increased verbose over 100
    - id parameter changed to input
    - added rel-base (09)
    - parameter mode 2 (rel)
    """

    def __init__(self, input=None):
        self.program = None
        self.asm = {
            1: self.asm_add,
            2: self.asm_mult,
            3: self.asm_input,
            4: self.asm_output,
            5: self.asm_jmp_if_true,
            6: self.asm_jmp_if_false,
            7: self.asm_less_than,
            8: self.asm_equal,
            9: self.asm_adj_rel_base,
            99: self.asm_halt
        }
        self.input = input
        self.rel_base = 0
        self.output = []

    def asm_halt(self, code):
        """ halt the computer """
        if verbose > 100: print 'HALT @', self.pc
        self.running = False
        return self

    def asm_add(self, code):
        """ add A + B -> C """
        ma, mb, mc = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code,2), self.decode_parameter_mode(code, 3)
        assert mc in [0,2], 'par.c has to have indirect(0)/relative(2) actual(%d) !' % mc
        # self.program[self.get_parameter(3)] = self.get_parameter(1, ma) + self.get_parameter(2, mb)
        a, b, c = self.get_parameter(1, ma), self.get_parameter(2, mb), self.get_parameter(3)
        if verbose > 100: print 'ADD: %s%d + %s%d -> %s%d' % ('@#r'[ma], a, '@#r'[mb], b, '@#r'[mc], c)
        value = a + b
        if mc == 0: self.program[c] = value
        if mc == 2: self.program[self.rel_base + c] = value
        self.pc += 4
        return self

    def asm_mult(self, code):
        """ mul A * B -> C """
        ma, mb, mc = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code,2), self.decode_parameter_mode(code, 3)
        assert mc in [0,2], 'par.c has to have indirect(0)/relative(2) actual(%d) !' % mc
        a, b, c = self.get_parameter(1, ma), self.get_parameter(2, mb), self.get_parameter(3)
        if verbose > 100: print 'MUL: %s%d * %s%d -> %s%d' % ('@#r'[ma], a, '@#r'[mb], b, '@#r'[mc], c)
        value = a * b
        if mc == 0: self.program[c] = value
        if mc == 2: self.program[self.rel_base + c] = value
        self.pc += 4
        return self

    def asm_input(self, code):
        """ takes a single integer as input and saves it to the address given by its only parameter """
        mode = self.decode_parameter_mode(code, par=1)
        assert mode in [0,2], 'INPUT par mode has to be indirect(0)/relative(2) actual(%d) !' % mode
        par = self.get_parameter(1)
        # get input from queue
        data = self.input.pop(0)
        if verbose > 100: print 'IN:', data, '-> @', par
        # store data
        if mode == 0: self.program[par] = data
        if mode == 2: self.program[self.rel_base + par] = data
        self.pc += 2
        return self

    def asm_output(self, code):
        """ outputs the value of its only parameter """
        mode = self.decode_parameter_mode(code, par=1)
        #assert mode in [0,2], 'OUPUT par mode has to be indirect(0)/relative(2) actual(%d) !' % mode
        data = self.get_parameter(1, mode)
        self.output.append(data)
        if verbose > 100: print 'OUT:', data
        self.pc += 2
        return self

    def asm_jmp_if_true(self, code):
        """ if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter """
        ma, mb = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code, 2)
        a, b = self.get_parameter(1, ma), self.get_parameter(2, mb)
        if verbose > 100: print 'JT: if %s%d != 0 jump %s%d' % ('@#r'[ma], a, '@#r'[mb], b)
        self.pc = b if a != 0 else self.pc + 3
        return self

    def asm_jmp_if_false(self, code):
        """ if the first parameter is zero, it sets the instruction pointer to the value from the second parameter """
        ma, mb = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code, 2)
        a, b = self.get_parameter(1, ma), self.get_parameter(2, mb)
        if verbose > 100: print 'JF: if %s%d == 0 jump %s%d' % ('@#r'[ma], a, '@#r'[mb], b)
        self.pc = b if a == 0 else self.pc + 3
        return self

    def asm_less_than(self, code):
        """ if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter.
        Otherwise, it stores 0 """
        ma, mb, mc = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code,2), self.decode_parameter_mode(code, 3)
        assert mc in [0,2], 'par.c has to have indirect(0)/relative(2) actual(%d) !' % mc
        a, b, c = self.get_parameter(1, ma), self.get_parameter(2, mb), self.get_parameter(3)
        if verbose > 100: print 'LT: %s%d < %s%d ? -> %s%d' % ('@#r'[ma], a, '@#r'[mb], b, '@#r'[mc], c)
        value = 1 if a < b else 0
        if mc == 0: self.program[c] = value
        if mc == 2: self.program[self.rel_base + c] = value
        self.pc += 4
        return self

    def asm_equal(self, code):
        """ if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter.
        Otherwise, it stores 0 """
        ma, mb, mc = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code,2), self.decode_parameter_mode(code, 3)
        assert mc in [0,2], 'par.c has to have indirect(0)/relative(2) actual(%d) !' % mc
        a, b, c = self.get_parameter(1, ma), self.get_parameter(2, mb), self.get_parameter(3)
        if verbose > 100: print 'EQ: %s%d = %s%d ? -> %s%d' % ('@#r'[ma], a, '@#r'[mb], b, '@#r'[mc], c)
        value = 1 if a == b else 0
        if mc == 0: self.program[c] = value
        if mc == 2: self.program[self.rel_base + c] = value
        self.pc += 4
        return self

    def asm_adj_rel_base(self, code):
        """ adjusts the relative base by the value of its only parameter """
        mode = self.decode_parameter_mode(code, 1)
        #assert ma in [1,2], 'par has to have immediate(1) mode actual(%d) !' % ma
        self.rel_base += self.get_parameter(1, mode)
        if verbose > 100: print 'REBASE:',self.rel_base
        self.pc += 2
        return self

    def decode_parameter_mode(self, code, par):
        """ return paremeter mode for parameter par 1-3 """
        return (code // 10 ** (1 + par)) % 10

    def decode_insctruction_code(self, code):
        """ return instruction code """
        return code % 100

    def get_parameter(self, par, mode=1):
        """ get parameter par=1,2,3 mode 0=indirect, 1=immediate, 2=relative """
        val = self.program[self.pc + par]
        assert mode in [0, 1, 2], 'Parameter mode has to be 0,1,2 only !'
        # 2=relative / 1=immediate / 0=address
        if mode == 0: return self.program[val]
        if mode == 1: return val
        if mode == 2: return self.program[self.rel_base + val]

    def step(self):
        """ execute one step at pc """
        try:
            code = self.program[self.pc]
        except IndexError:
            self.running = False
            if verbose > 100: print 'Out of program memory @', self.pc
            return
        if verbose > 100: print 'step code:', code, '@', self.pc
        asm_fnc = self.asm[self.decode_insctruction_code(code)]
        return asm_fnc(code)

    def program_load(self, prog, fill=2000):
        """ load csv string format to list """
        self.program = [int(i) for i in prog.split(',')]
        l = len(self.program)
        # add fill x zeros
        for i in range(fill):
            self.program.append(0)
        self.pc = 0
        self.running = False
        return l

    def run_prog(self, prog):
        """ execute program prog """
        l = self.program_load(prog)
        if verbose > 100: print 'Program length:', l, 'loaded ...'
        self.running = True
        while self.running:
            self.step()


class Boost:

    def __init__(self, input=None):
        self.comp = Computer3(input)

    def task_a(self, input):
        """ task A """
        self.comp.run_prog(input)
        result = self.comp.output[0] if len(self.comp.output) == 1 else self.comp.output
        return result

    def task_b(self, input):
        """ task B """
        return self.task_a(input)


def testcase(sut, input, result, task_b=False):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = f.readline()
    #
    print "TestCase", "B" if task_b else "A",
    print "for input:", data if 'data' in vars() else input,
    print "\t expected result:", result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========

# test cases
prog_echo = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
testcase(Boost(), prog_echo,  [ int(i) for i in prog_echo.split(',') ])
#
testcase(Boost(), '1102,34915192,34915192,7,4,7,99,0', 1219070632396864)
testcase(Boost(), '104,1125899906842624,99', 1125899906842624)

# 2453265701
testcase(Boost(input=[1]), None, 2453265701)

# ========
#  Task B
# ========

# 80805
testcase(Boost(input=[2]), None, 80805, task_b=True)

