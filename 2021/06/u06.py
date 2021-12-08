#!/usr/bin/env python3

__day__  = 6

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Lanternfish:

    def __init__(self):
        self.population = []
        self.reset_d = 6
        self.new_d   = 8
        self.spawn_d = -1

    def print(self, txt: str):
        print(txt, ','.join([ '%s' % f for f in self.population ]))

    def next_day(self):
        # dec timer
        population = [ f-1 for f in self.population ]
        # count expired
        spawn_num = population.count(self.spawn_d)
        # reset expired
        population = [ self.reset_d if f == self.spawn_d else f for f in population ]
        # spawn new
        self.population = population + [ self.new_d ] * spawn_num

    def task_a(self, input: list, days=80):
        """ task A """
        self.population = [int(i) for i in input[0].split(',')]
        if verbose: self.print('=init:')
        for d in range(1, days+1):
            self.next_day()
            if verbose: self.print('+%3dd:' % d)
        return len(self.population)

    def task_b(self, input: list, days=256):
        """ task B """
        return self.task_a(input, days)


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

testdata = [ "3,4,3,1,2" ]

# ========
#  Task A
# ========

# test cases
testcase_a(Lanternfish(), testdata,  5934)

# 351188
testcase_a(Lanternfish(),   None,     351188)

