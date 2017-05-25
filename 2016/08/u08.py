#!/usr/bin/env python

__motd__ = '--- Day 8: Two-Factor Authentication ---'

__url__ = 'http://adventofcode.com/2016/day/8'

verbose = 1

class PixelScreen:

    def __init__(self, width=50, height=6, state=0):
        self.width  = width
        self.height = height
        self.screen = [ [ state for x in range(width) ] for y in range(height) ]

    def get_screen(self, s0='.', s1='#'):
        return [ ''.join([s1 if x else s0 for x in row]) for row in self.screen ]

    def show(self, s0='.', s1='#'):
        for row in self.get_screen(s0, s1):
            print row

    def count_on(self):
        return sum([ row.count(1) for row in self.screen ])

    def rect_AxB(self, AxB):
        a,b = AxB.split('x')
        w,h = int(a),int(b)
        #
        for y in range(h):
            for x in range(w):
                self.screen[y][x] = 1

    def rot_row_A_byB(self, yby):
        " yby is string 'A by B' "
        a,_,b = yby.partition(' by ')
        by,row = int(b),int(a)
        # rotate cnt times
        for cnt in range(by):
            self.screen[row] = self.rshift(self.screen[row])

    def rot_col_A_byB(self, xby):
        " xby is string 'A by B' "
        a,_,b = xby.partition(' by ')
        by,col = int(b),int(a)
        # get lst from screen
        lst = [ self.screen[y][col] for y in range(self.height) ]
        # rotate cnt times
        for cnt in range(by):
            lst = self.rshift(lst)
        # back to screen
        for y,pix in enumerate(lst):
            self.screen[y][col] = pix

    def rshift(self, lst):
        lst.insert(0, lst.pop())
        return lst

    def instruction(self, str):
        " instruction parser and dispatcher "
        if str.startswith('rect '):
            axb = str.replace('rect ', '')
            self.rect_AxB(axb)
        if str.startswith('rotate row y='):
            abyb = str.replace('rotate row y=', '')
            self.rot_row_A_byB(abyb)
        if str.startswith('rotate column x='):
            abyb = str.replace('rotate column x=', '')
            self.rot_col_A_byB(abyb)

    def exec_file(self, fname):
        " execute instructions from file "
        with open(fname) as f:
            for line in f:
                if not line: continue
                self.instruction(line)
                if verbose:
                    print "Instruction:",line
                    self.show()
                    print


def testcase(input, result):
    " testcase verifies if input returns result "
    print "TestCase A"
    ps = PixelScreen(width=7, height=3)
    ps.exec_file(input)
    # verify
    for row,erow in zip(ps.get_screen(), result):
        print 'got:',row,"expected:",erow,'\t','OK' if row == erow else 'ERR'
    print

# ========
#  Task A
# ========


tcdata = __file__.replace('.py', '.tc.input')
tcscreen = [
    '.#..#.#',
    '#.#....',
    '.#.....'
]
# test cases
testcase(tcdata, tcscreen)

data = __file__.replace('.py', '.input')
ps = PixelScreen()
ps.exec_file(data)
r = ps.count_on()
# 123
print 'Task A input file:',data,'Result:',r
print

# ========
#  Task B
# ========

# AFBUPZBJPS
ps.show()
print
print 'Task B input file:',data,'Result: see the screen display above'
print
