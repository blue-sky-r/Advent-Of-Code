#!/usr/bin/env python3

__day__  = 3

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class BinDiag:

    def __init__(self):
        pass

    def count_bit_at_pos(self, data, pos0, bit01='0'):
        """ count bit chr01 at position pos0 (0-based starting from left) """
        bit_chr = [ s[pos0] for s in data ]
        return bit_chr.count(bit01)

    def most_at_pos(self, data, pos0, tie='-'):
        """ return the most common bit at position pos0 (from left) """
        threshold = len(data) / 2
        cnt0 = self.count_bit_at_pos(data, pos0, '0')
        if cnt0 > threshold: return '0'
        if cnt0 < threshold: return '1'
        return tie

    def least_at_pos(self, data, pos0, tie='-'):
        """ return the least common bit at position pos0 (from left) """
        threshold = len(data) / 2
        cnt0 = self.count_bit_at_pos(data, pos0, '0')
        if cnt0 < threshold: return '0'
        if cnt0 > threshold: return '1'
        return tie

    def gamma_rate(self, data):
        """ calc gamma rate """
        gamma = [ self.most_at_pos(data, pos0) for pos0 in range(len(data[0])) ]
        return int(''.join(gamma), 2)

    def epsilon_rate(self, data):
        """ calc epsilon rate """
        bin_max = 2**len(data[0]) - 1
        epsilon = bin_max - self.gamma_rate(data)
        return epsilon

    def filter_data_by_most_at_pos(self, data, pos0, tie='-'):
        """ filter only data with bit matching most at position pos0 """
        most = self.most_at_pos(data, pos0, tie)
        filtered = [ item for item in data if item[pos0] == most ]
        return filtered

    def filter_data_by_least_at_pos(self, data, pos0, tie='-'):
        """ filter only data with bit matching most at position pos0 """
        least = self.least_at_pos(data, pos0, tie)
        filtered = [ item for item in data if item[pos0] == least ]
        return filtered

    def filter_o2_data(self, data):
        """ filter data for O2 rate """
        for pos0 in range(len(data[0])):
            data = self.filter_data_by_most_at_pos(data, pos0, tie='1')
            if len(data) <= 1: break
        return data

    def filter_co2_data(self, data):
        """ filter data for CO2 rate """
        for pos0 in range(len(data[0])):
            data = self.filter_data_by_least_at_pos(data, pos0, tie='0')
            if len(data) <= 1: break
        return data

    def o2_rate(self, data):
        o2 = self.filter_o2_data(data)
        assert len(o2) == 1, 'ERROR - O2 filtering failed'
        return int(o2[0], 2)

    def co2_rate(self, data):
        co2 = self.filter_co2_data(data)
        assert len(co2) == 1, 'ERROR - CO2 filtering failed'
        return int(co2[0], 2)

    def task_a(self, input):
        """ task A """
        gamma = self.gamma_rate(input)
        epsilon = self.epsilon_rate(input)
        return gamma * epsilon

    def task_b(self, input):
        """ task B """
        o2 = self.o2_rate(input)
        co2 = self.co2_rate(input)
        return o2 * co2


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
            input = [ line.strip() for line in f ]
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

# ========
#  Task B
# ========

# test cases
testcase_b(BinDiag(), ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010'],  230)

# 3385170
testcase_b(BinDiag(),   None,     3385170)
