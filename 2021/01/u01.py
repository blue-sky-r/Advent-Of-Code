#!/usr/bin/env python3

__day__  = 1

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Sonar:

    def __init__(self):
        pass

    def add_measurements(self, depth_list):
        self.measurements = depth_list

    def calc_deltas(self):
        self.delta = [ b - a for a,b in zip(self.measurements[:-1], self.measurements[1:]) ]

    def calc_3sumdeltas(self):
        self.sums  = [ a+b+c for a,b,c in zip(self.measurements[:-2], self.measurements[1:], self.measurements[2:]) ]
        self.delta = [ b - a for a,b in zip(self.sums[:-1], self.sums[1:]) ]

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
        self.add_measurements(input)
        self.calc_3sumdeltas()
        return self.count_pos()


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

def testcase_b(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ int(line.strip()) for line in f ]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
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

# ========
#  Task A
# ========

# test cases
testcase_a(Sonar(), [199, 200, 208, 210, 200, 207, 240, 269, 260, 263],  7)

# 1564
testcase_a(Sonar(),   None,     1564)

# ========
#  Task B
# ========

# test cases
testcase_b(Sonar(), [199, 200, 208, 210, 200, 207, 240, 269, 260, 263],  5)

# 1611
testcase_b(Sonar(),   None,     1611)
