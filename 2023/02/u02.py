#!/usr/bin/env python3

__day__  = 2

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-01'

verbose = 0


class Bag:

    def __init__(self, cubes: dict):
        self.cubes = cubes

    def add_cubes(self, d1: dict, d2: dict) -> dict:
        """ add dictionaries d1 + d2 """
        d = { color:d1.get(color,0) + d2.get(color,0) for color in self.cubes }
        return d

    def are_cubes_within_limits(self, cubes: dict) -> bool:
        """ possible to have draw ? """
        within_limits = [ num <= self.cubes[color] for color,num in cubes.items() ]
        return all(within_limits)

    def is_game_valid(self, draws: list) -> bool:
        """ all draws are valid/possible """
        valid = [ self.are_cubes_within_limits(cubes) for cubes in draws ]
        return all(valid)

    def parse_cubes(self, drawtxt: str) -> dict:
        """ 3 blue, 4 red """
        cubes = {}
        for cube in drawtxt.split(','):
            n, color = cube.strip().split()
            cubes[color] = int(n)
        return cubes

    def parse_game(self, line: str):
        """ break line into parts """
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        draws = []
        gametxt, drawscsv = line.split(':')
        _, gamenr = gametxt.split()
        for drawtxt in drawscsv.split(';'):
            cubes = self.parse_cubes(drawtxt)
            draws.append(cubes)
        return int(gamenr), draws

    def task_a(self, input: list):
        """ task A """
        valid = []
        for game in input:
            gameid, draws = self.parse_game(game)
            if self.is_game_valid(draws):
                valid.append(gameid)
        return sum(valid)

    def task_b(self, input: list):
        """ task B """
        return None


def testcase_a(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
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
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

# ========
#  Task A
# ========

# cubes in bag
cubes = {'red':12, 'green':13, 'blue':14}

# test cases
testcase_a(Bag(cubes=cubes), testdata, 8)

# 1734
testcase_a(Bag(cubes=cubes), None, 1734)

# ========
#  Task B
# ========

# test cases
#testcase_b(C(), testdata,  2)

# 2
#testcase_b(C(),   None,    2)
