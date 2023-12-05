#!/usr/bin/env python3

__day__  = 3

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-03'

verbose = 0


class Schematic:

    def __init__(self):
        pass

    def chebyshev_distance(self, xy1, xy2) -> int:
        """ calc chebyshev distance https://en.wikipedia.org/wiki/Chebyshev_distance """
        def abs(a: int) -> int:
            """ absolute value of a """
            return a if a>= 0 else -a
        #
        dist = [ abs(xy2[0] - xy1[0]), abs(xy2[1] - xy1[1])]
        return max(dist)

    def build_map(self, input: list):
        """ build map dict[(x,y)] """
        self.map = {}
        for y,row in enumerate(input):
            for x,char in enumerate(row):
                if char == '.': continue
                self.map[(x,y)] = char

    def locate_numbers(self, input: list) -> list:
        """ locate numbers { 123 -> [xy1, xy2, ..] } """
        numbers = []
        for y,row in enumerate(input):
            val, xy = 0, []
            for x,char in enumerate(row):
                if char in '0123456789':
                    val = 10 * val + int(char)
                    xy.append((x,y))
                    continue
                if len(xy) > 0:
                    numbers.append( {val:xy} )
                    val, xy = 0, []
                    continue
            if len(xy) > 0:
                numbers.append( {val:xy} )
        return numbers

    def locate_parts(self) -> list:
        """ find all (x,y) of all parts """
        parts = [ xy for xy,char in self.map.items() if char not in '0123456789' ]
        return parts

    def part_number_distace(self, partxy: tuple, numberxy: list) -> int:
        """ distance between part and number """
        dist = [ self.chebyshev_distance(partxy, xy) for xy in numberxy ]
        return min(dist)

    def adjanced_values(self, parts: list, numbers: list) -> list:
        """ distance to part == 1 """
        adj = [ value \
                for part in parts \
                for number in numbers \
                for value,valuexy in number.items() \
                if self.part_number_distace(part, valuexy) == 1 ]
        return adj

    def locate_gears(self, numbers:list) -> list:
        """ find all (x,y) of all parts """
        gears = []
        potential_gear = [ xy \
                  for xy,char in self.map.items() \
                  if char == '*' ]
        for gear in potential_gear:
            adj = self.adjanced_values([gear], numbers)
            if len(adj) == 2:
                factor = adj[0] * adj[1]
                gears.append(factor)
        return gears

    def task_a(self, input: list):
        """ task A """
        self.build_map(input)
        numbers = self.locate_numbers(input)
        parts = self.locate_parts()
        values = self.adjanced_values(parts, numbers)
        return sum(values)

    def task_b(self, input: list):
        """ task B """
        self.build_map(input)
        numbers = self.locate_numbers(input)
        gears = self.locate_gears(numbers)
        return sum(gears)


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
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Schematic(), testdata, 4361)

# 521515
testcase_a(Schematic(),   None, 521515)

# ========
#  Task B
# ========

# test cases
testcase_b(Schematic(), testdata,  467835)

# 69527306
testcase_b(Schematic(),   None,  69527306)
