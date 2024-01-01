#!/usr/bin/env python3

__day__  = 14

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-01'

verbose = 0


import array

class Matrix:

    def __init__(self, typecode: str = 'i'):
        """ https://docs.python.org/3/library/array.html#module-array """
        self.typecode = typecode
        self.arr = array.array(self.typecode)

    def from_listoflists(self, lol: list):
        """  """
        self.rows = len(lol)
        self.cols = len(lol[0])
        for lst in lol:
            self.arr.fromlist(lst)
        return self

    def from_listofstr(self, los: list):
        """  """
        self.rows = len(los)
        self.cols = len(los[0])
        for s in los:
            self.arr.fromunicode(s)
        return self

    def _2d_to_linear(self, x: int, y: int) -> int:
        idx = y * self.cols + x
        return idx

    def setxy(self, x: int, y: int, val):
        idx = self._2d_to_linear(x, y)
        self.arr[idx] = val
        return self

    def getxy(self, x: int, y: int):
        idx = self._2d_to_linear(x, y)
        return self.arr[idx]

    xy = property(getxy, setxy)

    def getdimenstions(self) -> tuple:
        """ matrix dimension tuple """
        return (self.cols, self.rows)


class Dish:

    def __init__(self):
        pass

    def display(self, platform, msg = ''):
        """ debug print platform """
        print(msg)
        dimx, dimy = platform.getdimenstions()
        for y in range(dimy):
            row = [ platform.getxy(x,y) for x in range(dimx) ]
            print(' '.join(row))
        print()

    def slip_north(self, platform):
        """ """
        # dimensions
        dimx, dimy = platform.getdimenstions()
        # slide limits
        ylimits = [ 0 for x in range(dimx) ]
        # by rows
        for y in range(dimy):
            if verbose: self.display(platform, '--- y:%d ---' % y)
            for x in range(dimx):
                at = platform.getxy(x,y)
                # empty ?
                if at == '.': continue
                # square rock limits sliding
                if at == '#':
                    ylimits[x] = y+1
                    continue
                # round rock can slide
                if at == 'O':
                    slidetoy = ylimits[x]
                    if slidetoy != y:
                        platform.setxy(x,y, '.')
                        platform.setxy(x, slidetoy, 'O')
                    ylimits[x] = slidetoy + 1
        return

    def calc_load(self, platform):
        """ calc round rocks load """
        rounds = [ (platform.rows - y)  \
                   for y in range(platform.rows) \
                   for x in range(platform.cols) \
                   if platform.getxy(x,y) == 'O' ]
        return sum(rounds)

    def task_a(self, input: list):
        """ task A """
        #roundrocks, cuberocks = self.parse_platform(input)
        #roundrocks, cuberocks = self.tilt_north(roundrocks, cuberocks)
        platform = Matrix('u').from_listofstr(input)
        self.slip_north(platform)
        load = self.calc_load(platform)
        return load

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
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Dish(), testdata, 136)

# 108857
testcase_a(Dish(),  None, 108857)

