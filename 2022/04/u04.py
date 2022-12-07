#!/usr/bin/env python3

__day__  = 4

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class CampCleanup:

    def __init__(self):
        pass

    def get_range_ab(self, s):
        """ get numerical values a,b from range string a-b """
        a,b = s.split('-')
        return (int(a), int(b))

    def ab_within_cd(self, ab, cd):
        """ c.a.b.d """
        a,b = ab[0], ab[1]
        c,d = cd[0], cd[1]
        return (c <= a <= b) and (a <= b <= d)

    def ab_overlap_cd(self, ab, cd):
        """ c.a.d or c.b.d"""
        a,b = ab[0], ab[1]
        c,d = cd[0], cd[1]
        return (c <= a <= d) or (c <= b <= d)

    def task_a(self, input: list):
        """ task A """
        fully_contains = []
        for line in input:
            range_ab, range_cd = line.split(',')
            ab = self.get_range_ab(range_ab)
            cd = self.get_range_ab(range_cd)
            if self.ab_within_cd(ab, cd) or self.ab_within_cd(cd, ab):
                fully_contains.append(line)
        return len(fully_contains)

    def task_b(self, input: list):
        """ task B """
        overlap = []
        for line in input:
            range_ab, range_cd = line.split(',')
            ab = self.get_range_ab(range_ab)
            cd = self.get_range_ab(range_cd)
            if self.ab_overlap_cd(ab, cd) or self.ab_overlap_cd(cd, ab):
                overlap.append(line)
        return len(overlap)


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
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

# ========
#  Task A
# ========

# test cases
testcase_a(CampCleanup(), testdata,  2)

# 509
testcase_a(CampCleanup(),   None,  509)

# ========
#  Task B
# ========

# test cases
testcase_b(CampCleanup(), testdata,  4)

# 870
testcase_b(CampCleanup(),   None,  870)
