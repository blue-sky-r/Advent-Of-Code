#!/usr/bin/env python

__motd__ = '--- Day 5: Sunny with a Chance of Asteroids ---'

__url__ = 'http://adventofcode.com/2019/day/5'


verbose = 0


class Computer2:

    def __init__(self, input=[ 1 ]):
        self.program = None
        self.asm = {
             1: self.asm_add,
             2: self.asm_mult,
             3: self.asm_input,
             4: self.asm_output,
             5: self.asm_jmp_if_true,
             6: self.asm_jmp_if_false,
             7: self.asm_less_than,
             9: self.asm_equal,
            99: self.asm_halt
        }
        self.input  = input
        self.output = []

    def asm_halt(self, code):
        """ halt the computer """
        if verbose: print 'HALT @',self.pc
        self.running = False
        return self

    def asm_add(self, code):
        """ add A + B -> C """
        ma, mb, mc = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code,2), self.decode_parameter_mode(code, 3)
        assert mc == 0, 'par.c has to have indirect(0) mode !'
        self.program[self.get_parameter(3)] = self.get_parameter(1, ma) + self.get_parameter(2, mb)
        self.pc += 4
        return self

    def asm_mult(self, code):
        """ mul A * B -> C """
        ma, mb, mc = self.decode_parameter_mode(code,1), self.decode_parameter_mode(code, 2), self.decode_parameter_mode(code, 3)
        assert mc == 0, 'par.c has to have indirect(0) mode !'
        self.program[self.get_parameter(3)] = self.get_parameter(1, ma) * self.get_parameter(2, mb)
        self.pc += 4
        return self

    def asm_input(self, code):
        """ takes a single integer as input and saves it to the address given by its only parameter """
        mode = self.decode_parameter_mode(code, par=1)
        assert mode == 0, 'INPUT par mode has to be indirect(0) !'
        par = self.get_parameter(1)
        # get input from queue
        data = self.input.pop(0)
        if verbose: print 'IN:',data
        # store data
        self.program[par] = data
        self.pc += 2
        return self

    def asm_output(self, code):
        """ outputs the value of its only parameter """
        mode = self.decode_parameter_mode(code, par=1)
        #assert mode == 0, 'OUPUT par mode has to be indirect(0) !'
        data = self.get_parameter(1, mode)
        self.output.append(data)
        if verbose: print 'OUT:', data
        self.pc += 2
        return self

    def asm_jmp_if_true(self, code):
        """ if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter """
        ma, mb = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code, 2)
        self.pc = mb if ma != 0 else self.pc + 3
        return self

    def asm_jmp_if_false(self, code):
        """ if the first parameter is zero, it sets the instruction pointer to the value from the second parameter """
        ma, mb = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code, 2)
        self.pc = mb if ma == 0 else self.pc + 3
        return self

    def asm_less_than(self, code):
        """ if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter.
        Otherwise, it stores 0 """
        ma, mb = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code, 2)
        value = 1 if ma < mb else 0
        self.program[self.get_parameter(3)] = value
        return self

    def asm_equal(self, code):
        """ if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter.
        Otherwise, it stores 0 """
        ma, mb = self.decode_parameter_mode(code, 1), self.decode_parameter_mode(code, 2)
        value = 1 if ma == mb else 0
        self.program[self.get_parameter(3)] = value
        return self

    def decode_parameter_mode(self, code, par):
        """ return paremeter mode for parameter par 1-3 """
        return (code // 10**(1+par)) % 10

    def decode_insctruction_code(self, code):
        """ return instruction code """
        return code % 100

    def get_parameter(self, par, mode=1):
        """ get parameter par=1,2,3 mode 0=indirect, 1=immediate """
        par = self.program[self.pc + par]
        assert mode in [0,1], 'Parameter mode has to be 0,1 only !'
        # 1=immediate / 0=address
        return par if mode == 1 else self.program[par]

    def step(self):
        """ execute one step at pc """
        try:
            code = self.program[self.pc]
        except IndexError:
            self.running = False
            if verbose: print 'Out of program memory @', self.pc
            return
        if verbose: print 'DBG: executing code:', code,'@',self.pc
        asm_fnc = self.asm[self.decode_insctruction_code(code)]
        return asm_fnc(code)

    def program_load(self, prog):
        """ load csv string format to list """
        self.program = [int(i) for i in prog.split(',')]
        self.pc = 0
        self.running = False
        return self

    def run_prog(self, prog):
        """ execute program prog """
        self.program_load(prog)
        self.running = True
        while self.running:
            self.step()

    def task_a(self, input):
        """ task A """
        self.run_prog(input)
        return self.output.pop() if self.output else None

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
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    if verbose > 1: print 'Dump:',sut.program
    print

# ========
#  Task A
# ========

# test cases
testcase(Computer2(), '1002,4,3,4,33', None)

# 5182797
testcase(Computer2(),  None, 5182797, None)

# ========
#  Task b
# ========

