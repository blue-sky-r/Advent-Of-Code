#!/usr/bin/env python

__motd__ = '--- Day 1: The Tyranny of the Rocket Equation ---'

__url__ = 'http://adventofcode.com/2019/day/1'

import math

verbose = 0


class Spacecraft:

    def __init__(self):
        self.fuel = 0

    def fuel_for_module(self, mass):
        """ take its mass, divide by three, round down, and subtract 2 """
        return math.floor(mass / 3) - 2

    def add_module(self, mass):
        """ add module to spacecraft """
        self.fuel += self.fuel_for_module(mass)

    def task_a(self, input):
        """ task A """
        if type(input) == list:
            for i in input:
                self.add_module(i)
        else:
            self.add_module(input)
        return int(self.fuel)

    def task_b(self, input):
        """ task B """
        return


def testcase(sut, input, result, task_b=False):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ int(line.strip()) for line in f ]
    #
    print "TestCase", "B" if task_b else "A",
    print "for input:", data if 'data' in vars() else input,
    print "\t expected result:", result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    #r = f.find_duplo(input) if task_b else f.change_seq(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========

# test cases
testcase(Spacecraft(),     12,     2)
testcase(Spacecraft(),     14,     2)
testcase(Spacecraft(),   1969,   654)
testcase(Spacecraft(), 100756, 33583)

# 3303995
testcase(Spacecraft(),   None,  3303995)
