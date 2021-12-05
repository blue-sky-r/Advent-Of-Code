#!/usr/bin/env python3

__day__  = 3

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class BinDiag:

    def __init__(self):
        pass

    def add_data(self, data):
        """ add binary diagnostic data """
        self.data = data

    def count_bit_at_pos(self, pos0, bit01='0'):
        """ count bit chr01 at position pos0 (0-based starting from left) """
        bit_chr = [ s[pos0] for s in self.data ]
        return bit_chr.count(bit01)

    def most_at_pos(self, pos0, tie='-'):
        """ return the most common bit at position pos0 (from left) """
        threshold = len(self.data) / 2
        cnt0 = self.count_bit_at_pos(pos0, '0')
        if cnt0 > threshold: return '0'
        if cnt0 < threshold: return '1'
        return tie

    def gamma_rate(self):
        """ calc gamma rate """
        gamma = [ self.most_at_pos(pos0) for pos0 in range(len(self.data[0])) ]
        return int(''.join(gamma), 2)

    def epsilon_rate(self):
        """ calc epsilon rate """
        bin_max = 2**len(self.data[0]) - 1
        epsilon = bin_max - self.gamma_rate()
        return epsilon

    def o2_rate(self):
        """ calc oxygen rating """
        for pos0 in range(len(self.data[0])):
            bit01X = self.most_at_pos(pos0)

    def task_a(self, input):
        """ task A """
        self.add_data(input)
        gamma = self.gamma_rate()
        epsilon = self.epsilon_rate()
        return gamma * epsilon

    def task_b(self, input):
        """ task B """
        return None


def testcase_a(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
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
testcase_a(BinDiag(), ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010'],  198)

# 3882564
testcase_a(BinDiag(),   None,     3882564)


