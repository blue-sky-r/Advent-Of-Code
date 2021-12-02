#!/usr/bin/env python3

__day__  = 1

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0

from functools import reduce


class Sonar:

    def __init__(self):
        pass

    def add_measurements(self, depth_list):
        self.measurements = depth_list

    def calc_deltas(self):
        """ count deltas """
        self.delta = []
        iterator = iter(self.measurements)
        last = next(iterator)
        for d in iterator:
            self.delta.append(d - last)
            last = d

    def count_pos(self):
        return len([ d for d in self.delta if d > 0 ])

    def count_neg(self):
        return len([ d for d in self.delta if d < 0 ])

    def task_a(self, input):
        """ task A """
        self.add_measurements(input)
        self.calc_deltas()
        return self.count_pos()

    def task_b(self, input):
        """ task B """
        return None


def testcase_a(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ int(line.strip()) for line in f ]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

# ========
#  Task A
# ========

# test cases
testcase_a(Sonar(), [199, 200, 208, 210, 200, 207, 240, 269, 260, 263],  7)

# 1564
testcase_a(Sonar(),   None,     1564)
