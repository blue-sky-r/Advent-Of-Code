#!/usr/bin/env python3

__day__  = 7

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Crabs:

    def __init__(self):
        pass

    def init_pos_csv(self, line: str):
        self.subs = list(map(int, line.split(',')))

    def fuel_for_position_dist(self, pos: int):
        """ fuel is just distance d=abs(an-a1) """
        dist = [ abs(pos-s) for s in self.subs ]
        return sum(dist)

    def fuel_for_alignment_a(self):
        maxpos = max(self.subs)
        ffal = [ (pos, self.fuel_for_position_dist(pos)) for pos in range(1, maxpos+1) ]
        return dict(ffal)

    def fuel_for_position_aritseq(self, pos: int):
        """ fuel is arithmetic sequence s=(a1+an)*n/2 """
        dist = [ (1+abs(pos-s))*abs(pos-s)//2 for s in self.subs ]
        return sum(dist)

    def fuel_for_alignment_b(self):
        maxpos = max(self.subs)
        ffal = [ (pos, self.fuel_for_position_aritseq(pos)) for pos in range(1, maxpos+1) ]
        return dict(ffal)

    def task_a(self, input: list):
        """ task A """
        self.init_pos_csv(input[0])
        # dictionary pos -> fuel
        posfuel = self.fuel_for_alignment_a()
        # position with min fuel
        minpos = min(posfuel, key=posfuel.get)
        # return min fuel
        return posfuel[minpos]

    def task_b(self, input: list):
        """ task B """
        self.init_pos_csv(input[0])
        # dictionary pos -> fuel
        posfuel = self.fuel_for_alignment_b()
        # position with min fuel
        minpos = min(posfuel, key=posfuel.get)
        # return min fuel
        return posfuel[minpos]


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

testdata = ["16,1,2,0,4,2,7,1,2,14"]

# ========
#  Task A
# ========

# test cases
testcase_a(Crabs(), testdata,  37)

# 336701
testcase_a(Crabs(),   None,    336701)

# ========
#  Task B
# ========

# test cases
testcase_b(Crabs(), testdata,  168)

# 95167302
testcase_b(Crabs(),   None,    95167302)
