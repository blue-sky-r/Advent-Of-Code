#!/usr/bin/env python3

__day__  = 11

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-12'

verbose = 0


class GalaxyMap:

    def __init__(self, empty_multilier=1):
        self.empty_multiplier = empty_multilier

    def taxicab_distance(self, xy1: tuple, xy2: tuple, empties: list) -> int:
        """ calc taxicab distance between xy1 and xy2 """
        def abs(v: int) -> int:
            """ abs value """
            return v if v >= 0 else -v
        # how many empty rows/columns are included in calculated distance
        includedemptyx = [ x for x in empties[0] if min(xy1[0], xy2[0]) < x < max(xy1[0], xy2[0]) ]
        includedemptyy = [ y for y in empties[1] if min(xy1[1], xy2[1]) < y < max(xy1[1], xy2[1]) ]
        absdx = abs(xy2[0] - xy1[0]) + len(includedemptyx) * (self.empty_multiplier - 1)
        absdy = abs(xy2[1] - xy1[1]) + len(includedemptyy) * (self.empty_multiplier - 1)
        return absdx + absdy

    def multiply_empty_lines(self, input: list, mult: int = 2) -> list:
        """ double empty lines """
        expanded_map = []
        # double empty lines
        for line in input:
            expanded_map.append(line)
            # line empty ?
            if line.count('#') == 0:
                for i in range(mult-1):
                    expanded_map.append(line)
        return expanded_map

    def transpose_map(self, gmap: list) -> list:
        """ transpose row to columns  """
        transposed = []
        for col in range(len(gmap[0])):
            trow = [ line[col] for line in gmap ]
            transposed.append(trow)
        return transposed

    def empty_rows(self, gmap: list) -> list:
        """ get y coordinates of empty rows """
        empties = []
        for y,line in enumerate(gmap):
            if line.count('#') == 0:
                empties.append(y)
        return empties

    def parse_galaxymap(self, input: list) -> tuple:
        """ parse galaxy map and process expansion """
        # identify empties
        emptiesy = self.empty_rows(input)
        tinput = self.transpose_map(input)
        emptiesx = self.empty_rows(tinput)
        # extract galaxies
        galaxies = []
        for y,line in enumerate(input):
            for x,c in enumerate(line):
                if c == '#':
                    galaxies.append((x,y))
        return galaxies, (emptiesx, emptiesy)

    def calc_distances(self, galaxies: list, empties: list) -> list:
        """ calc distanec between galaxies pairs """
        dist = []
        for dfrom in range(len(galaxies)):
            for dto in range(dfrom+1, len(galaxies)):
                d = self.taxicab_distance(galaxies[dfrom], galaxies[dto], empties)
                if verbose: print('dist: ',dfrom+1,'->',dto+1,'=',d)
                dist.append(d)
        return dist

    def task_a(self, input: list):
        """ task A """
        galaxies, empties = self.parse_galaxymap(input)
        distances = self.calc_distances(galaxies, empties)
        return sum(distances)

    def task_b(self, input: list):
        """ task B """
        galaxies, empties = self.parse_galaxymap(input)
        distances = self.calc_distances(galaxies, empties)
        return sum(distances)


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
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

# ========
#  Task A
# ========

# test cases
testcase_a(GalaxyMap(empty_multilier=2), testdata, 374)

# 10077850
testcase_a(GalaxyMap(empty_multilier=2), None, 10077850)

# ========
#  Task B
# ========

# test cases
testcase_b(GalaxyMap(empty_multilier=10), testdata, 1030)

# test cases
testcase_b(GalaxyMap(empty_multilier=100), testdata, 8410)

# 504715068438
testcase_b(GalaxyMap(empty_multilier=1000000), None, 504715068438)
