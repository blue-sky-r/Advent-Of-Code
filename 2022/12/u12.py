#!/usr/bin/env python3

__day__  = 12

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2022-12-06'

verbose = 0


class HillClimbing:

    def __init__(self):
        self.map = []

    def get(self, xy, outside=None):
        row, col = xy[1], xy[0]
        if 0 <= row < len(self.map) and 0 <= col < len(self.map[0]):
            return self.map[row][col]
        return outside

    def avail_moves(self, xy):
        val = self.get(xy)
        if val is None: return
        x,y = xy[0], xy[1]
        r = []
        for xxyy in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            vval = self.get(xxyy)
            if vval is None: continue
            if vval > val+1: continue
            r.append(xxyy)
        return r

    def find_path(self, srcxy, dstxy, path):
        # destination reached
        if srcxy == dstxy: return True, []
        for xy in self.avail_moves(srcxy):
            if xy in path: continue
            r, p = self.find_path(xy, dstxy, path + [xy])
            
        return False, path

    def walk(self, srcxy, dstxy, path=None):
        """ walk from scrxy -> dstxy"""
        # handle default to avoid mutable default par
        if path is None:
            path = []
        # destination reached
        if srcxy == dstxy:
            yield path
        # try all valid moves
        for xy in self.avail_moves(srcxy):
            # ignore if already been @xy
            if xy in path:
                continue
            # walk recurs. from new position
            for p in self.walk(xy, dstxy, path + [xy]):
                yield p

    def task_a(self, input: list):
        """ task A """
        for row, line in enumerate(input):
            if 'S' in line:
                startxy = (line.index('S'), row)
                line = line.replace('S', 'a')
            if 'E' in line:
                endxy = (line.index('E'), row)
                line = line.replace('E', 'z')
            self.map.append([ord(c) - ord('a') for c in line])
        #
        length = []
        for path in self.walk(startxy, endxy):
            length.append(len(path))
            if verbose: print(len(path), path)
        return min(length)

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
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

# ========
#  Task A
# ========

# test cases
testcase_a(HillClimbing(), testdata,  31)

# ? correct, but does not finish in reasonable time
# FODO: faster implementation
testcase_a(HillClimbing(),   None,     1)

