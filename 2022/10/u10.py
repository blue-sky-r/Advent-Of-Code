#!/usr/bin/env python3

__day__  = 10

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 1


class CPU:

    def __init__(self, cols=40, rows=6):
        self.X = 1
        self.CLK = 1
        self.signalstrength = 0
        self.ssupdate = {
            'ofs': -20,
            'each': 40
        }
        self.ins_set = {
            'noop': self._noop,
            'addx': self._addx
        }
        self.rows, self.cols = rows, cols
        self.spritelen = 3
        self.crt_pixels = []
        self.clk_cycle()

    def print_crt(self, txt=''):
        """ visualize crt """
        if not verbose: return
        print(txt)
        for row in range(self.rows):
            line = [ '#' if (row*self.cols+col) in self.crt_pixels else '.' for col in range(self.cols) ]
            print(''.join(line))
        print()

    def _noop(self, v=None):
        self.CLK += 1
        self.clk_cycle()

    def _addx(self, v):
        self.CLK += 1
        self.clk_cycle()
        self.CLK += 1
        self.X += v
        self.clk_cycle()

    def update_signalstrength(self):
        """ update 20th + each 40th clk cycle """
        update_cycle = (self.CLK + self.ssupdate['ofs']) % self.ssupdate['each']
        if update_cycle == 0:
            self.signalstrength += self.CLK * self.X
            if verbose: print('update_signalstrength() CLK=',self.CLK, 'X=',self.X, 'ss=',self.signalstrength)

    def clk_cycle(self):
        """ cpu clock cycle """
        self.update_signalstrength()
        self.pixel()

    def pixel(self):
        """ active crt pixels """
        row_x = (self.CLK-1) % self.cols
        sprite = [ row_x-1, row_x, row_x+1 ]
        if self.X in sprite:
            self.crt_pixels.append(self.CLK-1)

    def exec(self, instruction):
        """  """
        ins, par = instruction, None
        has_par = ' ' in instruction
        if has_par:
            ins, par = instruction.split()
            par = int(par)
        fnc = self.ins_set.get(ins)
        fnc(par)

    def task_a(self, input: list):
        """ task A """
        for instruction in input:
            self.exec(instruction)
        return self.signalstrength

    def task_b(self, input: list):
        """ task B """
        for instruction in input:
            self.exec(instruction)
        self.print_crt('- result -')
        return self.signalstrength


def testcase_a(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_b(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()


# ======
#  MAIN
# ======

print()
print(__motd__, __url__)
print()

testdata = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

# ========
#  Task A
# ========

# test cases
testcase_a(CPU(), testdata,  13140)

# 14860
testcase_a(CPU(),   None,    14860)

# ========
#  Task B
# ========

# test cases
testcase_b(CPU(), testdata, 13140)

# RGZEHURK
testcase_b(CPU(),   None,   14860)
