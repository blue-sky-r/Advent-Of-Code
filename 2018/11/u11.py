#!/usr/bin/env python

__motd__ = '--- Day 11: Chronal Charge ---'

__url__ = 'http://adventofcode.com/2018/day/11'


verbose = 0


class Grid:

    def __init__(self, serial, size=300):
        self.serial = serial
        self.size = size
        self.power_level = {}

    def hundreds(self, v):
        """ get only hundreds num """
        return int(v / 100) % 10

    def cell_power_level(self, x,y):
        """ calc power level at x,y """
        rack_id = (x + 10)
        plevel = rack_id * y
        plevel = plevel + self.serial
        plevel = plevel * rack_id
        plevel = self.hundreds(plevel)
        plevel = plevel - 5
        if verbose > 4: print "cell_power_level(x:",x,"y:",y,") -> ",plevel
        return plevel

    def recalc(self):
        """ recalc entire grid power levels """
        self.power_level = dict([ ( (x,y), self.cell_power_level(x,y) ) for x in range(1, self.size+1) for y in range(1, self.size+1) ])

    def square_power_level(self, topleftx, toplefty, size=3):
        """ calc square power level """
        if topleftx+size > self.size or toplefty+size > self.size:
            # invalid square - outside of the grid
            return None
        spl = sum([ self.power_level[(x,y)] for x in range(topleftx, topleftx+size) for y in range(toplefty, toplefty+size) ])
        if verbose > 3: print "square_power_level(x:",topleftx,"y:",toplefty,"size:",size,") = ",spl
        return spl

    def find_max_spl(self, squaresize=3):
        """ find the max square power level """
        # chyba dict()
        spl = dict([ ( (x,y), self.square_power_level(x,y, squaresize) ) for x in range(1, self.size-squaresize) for y in range(1, self.size-squaresize) ])
        maxspl = max(spl, key=spl.get)
        if verbose > 2: print "find_max_spl(sqaresize:",squaresize,") = ",spl[maxspl],"@",maxspl
        return maxspl, spl[maxspl]

    def find_max_square_size_old(self):
        """ find square size to produce max power - brute force method = very slow """
        mss = dict([(size, self.find_max_spl(size)) for size in range(1, self.size + 1)])
        maxss = max(mss, key=mss.get)
        if verbose > 1: print "find_max_square_size() = ", mss[maxss], "@", maxss
        return maxss, mss[maxss]

    def find_max_square_size(self):
        """ find square size to produce max power using delta criteria (difference) """
        # init
        spl_last = self.find_max_spl(1)
        # iterate while delta is positive => value is increasing
        for size in range(2, self.size+1):
            spl_act = self.find_max_spl(size)
            # delta of max. square power level
            delta = spl_act[1] - spl_last[1]
            # if delta is <= 0, stop and return previous value
            if delta < 0:
                if verbose > 1: print "find_max_square_size() = ", spl_last,"@",size-1
                return size-1, spl_last
            spl_last = spl_act

    def input_line(self, str):
        """ -11 """
        return str[0],str[1]

    def task_a(self, input):
        """ task A """
        for line in input:
            x,y = self.input_line(line)
        #r = self.cell_power_level(x, y)
        # recalc antire grid
        self.recalc()
        xy, val = self.find_max_spl()
        return xy, val

    def task_b(self, input):
        """ task B """
        for line in input:
            x, y = self.input_line(line)
        # recalc antire grid
        self.recalc()
        size, xy_plevel = self.find_max_square_size()
        xy, plevel = xy_plevel
        return xy, plevel, size


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

# test cases
#testcase(Grid(serial=8),  [(  3,   5)],  4)
#testcase(Grid(serial=57), [(122,  79)], -5)
#testcase(Grid(serial=39), [(217, 196)],  0)
# testcase(Grid(serial=71), [(101, 153)],  4)

#testcase(Grid(serial=18), [], ((33, 45), 29))
#testcase(Grid(serial=42), [], ((21, 61), 30))

# ((19, 17), 29)
#testcase(Grid(serial=7989), [], ((19, 17), 29))

# ========
#  Task B
# ========

# test cases
testcase(Grid(serial=18), [], (( 90,269), 113, 16), task_b=True)
testcase(Grid(serial=42), [], ((232,251), 119, 12), task_b=True)

# (233, 286), 132, 12 wrong: 233,286,12 ???
testcase(Grid(serial=7989), [], ((233, 286), 132, 12), task_b=True)
