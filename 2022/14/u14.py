#!/usr/bin/env python3

__day__  = 14

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class RegolithReservoir:

    def __init__(self):
        self.symbol = {
            'rock': '#',
            'air': '.',
            'source': '+',
            'sand': 'o'
        }
        self.map = {}

    def print(self, txt=''):
        """ visualize map """
        if not verbose: return
        if txt: print(txt)
        for y in range(self.lowhighy[0], self.lowhighy[1]+1):
            row = [ self.map[(x,y)] for x in range(self.lowhighx[0], self.lowhighx[1]+1) ]
            print(''.join(row))
        print()

    def parse_line(self, line: str):
        """ '498,4 -> 498,6 -> 496,6' to [(498, 4), (498, 6), (496, 6)] """
        listoftuples = [(int(l[0]), int(l[1])) for l in [xy.split(',') for xy in line.split(' -> ')]]
        return listoftuples

    def parse(self, input: list):
        """ parse input to rocks list of xy tuples """
        rocks = []
        for line in input:
            rocks.append(self.parse_line(line))
        return rocks

    def build_map(self, rocks: list, sand=(500,0)):
        """ build map from rocks definition """
        # extract x and y values
        x = [ xy[0] for rock in rocks for xy in rock ] + [sand[0]]
        y = [ xy[1] for rock in rocks for xy in rock ] + [sand[1]]
        # find min-max-xy
        minx, maxx = min(x), max(x)
        miny, maxy = min(y), max(y)
        lowx, highx = minx-1, maxx+1
        lowy, highy = miny, maxy+1
        # store
        self.lowhighx = lowx, highx
        self.lowhighy = lowy, highy
        # fill map with air
        self.map = dict([ ((x,y), self.symbol['air']) for x in range(lowx, highx+1) for y in range(lowy, highy+1) ])
        # add rocks
        for rock in rocks:
            for startxy, endxy in zip(rock[:-1], rock[1:]):
                dx, dy = endxy[0] - startxy[0], endxy[1] - startxy[1]
                xy = startxy
                self.map[xy] = self.symbol['rock']
                while xy != endxy:
                    if dx > 0: xy = (xy[0]+1,xy[1])
                    if dx < 0: xy = (xy[0]-1,xy[1])
                    if dy > 0: xy = (xy[0],xy[1]+1)
                    if dy < 0: xy = (xy[0],xy[1]-1)
                    self.map[xy] = self.symbol['rock']
        # add sand output
        self.map[sand] = self.symbol['source']

    def sand_fall(self, xy):
        """ single sand unit fall from xy
        returns: xy of sand unit end loc, True sand is falling through, False xy is block
        """
        # falling out of the map
        if xy[1] >= self.lowhighy[1]:
            return True
        freefall, blocked = [self.symbol['air']], [self.symbol['rock'], self.symbol['sand']]
        # down, left, right
        downxy, leftxy, rightxy = (xy[0], xy[1]+1), (xy[0]-1, xy[1]+1), (xy[0]+1, xy[1]+1)
        # current position is block
        if self.map[xy] in blocked:
            return False
        # try fall down, left, right
        for dlrxy in [downxy, leftxy, rightxy]:
            r = self.sand_fall(dlrxy)
            if r: return r
        # cannot fall down/left/right = stay here
        self.map[xy] = self.symbol['sand']
        return xy

    def task_a(self, input: list):
        """ task A """
        rocks = self.parse(input)
        self.build_map(rocks)
        self.print('initial state')
        for i in range(1000):
            r = self.sand_fall((500,0))
            if r == True: break
            self.print('%s pieces of sand - result %s' % ((i+1), r))
        return i

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
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

# ========
#  Task A
# ========

# test cases
testcase_a(RegolithReservoir(), testdata,  24)

# 728
testcase_a(RegolithReservoir(),   None,   728)

