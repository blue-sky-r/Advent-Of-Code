#!/usr/bin/env python3

__day__  = 13

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 2


class TransarentOrigami:

    def __init__(self):
        self.paper = []

    def init_paper(self, input: list):
        for line in input:
            if not line: break
            x,y = list(map(int, line.split(',')))
            self.paper.append((x,y))

    def print(self, msg:str, limits=(40,10), symbols='.#'):
        maxx, maxy = max([x for x,y in self.paper]), max([y for x,y in self.paper])
        print('=',msg,'= dots:',len(self.paper),'= max:',(maxx,maxy),'=')
        if verbose < 2: return
        for y in range(min(maxy+1,limits[1])):
            for x in range(min(maxx+1,limits[0])):
                print(symbols[1] if (x,y) in self.paper else symbols[0], end='')
            print(end='\n')
        print

    def fold_y(self, foldy:int):
        # transfer everything below foldy
        below = [ (x,y) for x,y in self.paper if y < foldy ]
        # fold everything above foldy
        above = [ (x,2 * foldy - y) for x,y in self.paper if y > foldy ]
        # errors - exactly on fold
        errors = [ (x,y) for x,y in self.paper if y == foldy ]
        # consilidate to avoid duplicities
        self.paper = below + [ xy for xy in above if xy not in below ]
        # optional display errors
        if verbose and errors:
            print('ERR - fold_y(',foldy,') dots on fold:',' '.join(errors))

    def fold_x(self, foldx:int):
        # transfer everything below foldx
        below = [ (x,y) for x,y in self.paper if x < foldx ]
        # fold everything above foldx
        above = [ (2 * foldx - x,y) for x,y in self.paper if x > foldx ]
        # errors - exactly on fold
        errors = [ (x,y) for x,y in self.paper if x == foldx ]
        # consilidate to avoid duplicities
        self.paper = below + [ xy for xy in above if xy not in below ]
        # optional display errors
        if verbose and errors:
            print('ERR - fold_x(',foldx,') dots on fold:',' '.join(errors))

    def fold(self, input: list, filter='fold along ', limit=0):
        """ fold along x=5, fold along y=7 """
        for step,fa in enumerate([line for line in input if line.startswith(filter)]):
            xy,num = fa.replace(filter,'').split('=')
            if xy == 'x':
                self.fold_x(int(num))
            if xy == 'y':
                self.fold_y(int(num))
            if verbose: self.print(fa)
            if limit > 0 and step+1 >= limit:
                break

    def count_visible_dots(self):
        return len(self.paper)

    def task_a(self, input: list):
        """ task A """
        self.init_paper(input)
        if verbose: self.print('init')
        self.fold(input, limit=1)
        self.print('result')
        return self.count_visible_dots()

    def task_b(self, input: list):
        """ task B """
        self.init_paper(input)
        if verbose: self.print('init')
        self.fold(input)
        self.print('result')
        return self.count_visible_dots()


def testcase_a(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.strip() for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.strip() for line in input.splitlines() ]
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
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

# ========
#  Task A
# ========

# test cases
testcase_a(TransarentOrigami(), testdata,  17)

# 737
testcase_a(TransarentOrigami(),   None,   737)

# ========
#  Task B
# ========

# 0 - visual check
testcase_b(TransarentOrigami(), testdata,  16)

# ZUJUAFHP - visual check
testcase_b(TransarentOrigami(),   None,    96)
