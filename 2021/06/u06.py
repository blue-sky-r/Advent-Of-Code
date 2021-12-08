#!/usr/bin/env python3

__day__  = 6

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Lanternfish:

    def __init__(self):
        self.population = {}
        self.reset_d = 6
        self.new_d   = 8

    def print(self, txt: str):
        print(txt, ''.join([ ('%s,' % day)*cnt for day,cnt in self.population.items() ])[:-1],'\t pop=',self.count_population())

    def init_population(self, line: str):
        """ init by CSV string """
        for f in line.split(','):
            day = int(f)
            self.population[day] = self.population.get(day, 0) + 1

    def next_day(self):
        new_population = {}
        for day,cnt in self.population.items():
            new_day = day - 1
            if new_day >= 0:
                new_population[new_day] = new_population.get(new_day, 0) + cnt
            else:
                new_population[self.reset_d] = new_population.get(self.reset_d, 0) + cnt
                new_population[self.new_d]   = new_population.get(self.new_d, 0)   + cnt
        self.population = new_population

    def count_population(self):
        cnt = sum(self.population.values())
        return cnt

    def task_a(self, input: list, days=80):
        """ task A """
        self.init_population(input[0])
        if verbose: self.print('=init:')
        for d in range(1, days+1):
            self.next_day()
            if verbose: self.print('+%3dd:' % d)
        return self.count_population()

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

# ========
#  Task B
# ========

# test cases
testcase_b(Lanternfish(), testdata,    26984457539)

# 1595779846729
testcase_b(Lanternfish(),   None,    1595779846729)
