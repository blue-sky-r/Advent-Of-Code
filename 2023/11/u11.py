#!/usr/bin/env python3

__day__  = 11

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-12'

verbose = 0


class GalaxyMap:

    def __init__(self):
        pass

    def taxicab_distance(self, xy1: tuple, xy2: tuple) -> int:
        """ calc taxicab distance between xy1 and xy2 """
        def abs(v: int) -> int:
            """ abs value """
            return v if v >= 0 else -v
        absdx, absdy = abs(xy2[0] - xy1[0]), abs(xy2[1] - xy1[1])
        return absdx + absdy

    def double_empty_lines(self, input: list) -> list:
        """ double empty lines """
        expanded_map = []
        # double empty lines
        for line in input:
            expanded_map.append(line)
            # line empty ?
            if line.count('#') == 0:
                expanded_map.append(line)
        return expanded_map

    def transpose_map(self, gmap: list) -> list:
        """ transpose row to columns  """
        transposed = []
        for col in range(len(gmap[0])):
            trow = [ line[col] for line in gmap ]
            transposed.append(trow)
        return transposed

    def parse_galaxymap(self, input: list) -> list:
        """ parse galaxy map and process expansion """
        gmap = input
        # process expansion
        gmap = self.double_empty_lines(gmap)
        gmap = self.transpose_map(gmap)
        gmap = self.double_empty_lines(gmap)
        gmap = self.transpose_map(gmap)
        # extract galaxies
        galaxies = []
        for y,line in enumerate(gmap):
            for x,c in enumerate(line):
                if c == '#':
                    galaxies.append((x,y))
        return galaxies

    def calc_distances(self, galaxies: list) -> list:
        """ calc distanec between galaxies pairs """
        dist = []
        for dfrom in range(len(galaxies)):
            for dto in range(dfrom+1, len(galaxies)):
                d = self.taxicab_distance(galaxies[dfrom], galaxies[dto])
                if verbose: print('dist: ',dfrom,'->',dto,'=',d)
                dist.append(d)
        return dist

    def task_a(self, input: list):
        """ task A """
        galaxies = self.parse_galaxymap(input)
        distances = self.calc_distances(galaxies)
        return sum(distances)

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
testcase_a(GalaxyMap(), testdata, 374)

# 10077850
testcase_a(GalaxyMap(), None, 10077850)

