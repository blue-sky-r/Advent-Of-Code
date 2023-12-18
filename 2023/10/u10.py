#!/usr/bin/env python3

__day__  = 10

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-01'

verbose = 0


class PipeMaze:

    def __init__(self):
        pass

    def parse_maze(self, input: list) -> tuple:
        """ """
        maze, start = {}, None
        for y,line in enumerate(input):
            for x,c in enumerate(line):
                xy = (x,y)
                if c == 'S': maze[xy], start = 'EWNS', xy
                if c == '-': maze[xy] = 'EW'
                if c == '|': maze[xy] = 'NS'
                if c == '7': maze[xy] = 'WS'
                if c == 'J': maze[xy] = 'NW'
                if c == 'L': maze[xy] = 'NE'
                if c == 'F': maze[xy] = 'SE'
        return maze, start

    def is_pipe_connected(self, maze: dict, start: tuple, dir: str) -> tuple:
        """ maximum recursion depth exceeded in comparison """
        x, y = start[0], start[1]
        xwest, xeast = x-1, x+1
        ynorth, ysouth = y-1, y+1
        # E -> W connection
        if dir == 'E' and 'W' in maze.get((xeast,y),''):
            return (xeast,y)
        # W -> E connection
        if dir == 'W' and 'E' in maze.get((xwest,y),''):
            return (xwest,y)
        # N -> S connection
        if dir == 'N' and 'S' in maze.get((x,ynorth),''):
            return (x,ynorth)
        # S -> N connection
        if dir == 'S' and 'N' in maze.get((x,ysouth),''):
            return (x,ysouth)

    def find_pipe_loop(self, maze: dict, start: tuple, dirs: str) -> list:
        """ start at start and move to locate loop in a maze, return found loop """
        act, path = start, [start]
        while True:
            # possible moves from act position
            xys = [ xy for xy in [ self.is_pipe_connected(maze, act, step) for step in dirs ] if xy and xy != act ]
            # loop found ?
            if start in xys and len(path) > 4:
                return path
            # filterout already visited
            xys = [ xy for xy in xys if xy not in path ]
            # debug
            if verbose: print('at', act, 'maze:', maze[act], 'possible moves', xys)
            # no possible moves, got stacked
            if len(xys) == 0:
                return
            # take the first move (should be only 1)
            act = xys[0]
            dirs = maze[act]
            path.append(act)

    def locate_pipeloop(self, maze: dict, start: tuple) -> tuple:
        """ locate the pipe loop starting from start """
        for step in 'WNSE':
            loop = self.find_pipe_loop(maze, start, step)
            if loop:
                return loop

    def task_a(self, input: list):
        """ task A """
        maze, start = self.parse_maze(input)
        loop = self.locate_pipeloop(maze, start)
        if verbose: print('loop:', loop)
        #dist = self.locate_pipeloop(pipe, start)
        return int(len(loop) / 2)

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

# ========
#  Task A
# ========

testdata = """
.....
.S-7.
.|.|.
.L-J.
.....
"""

# test cases
testcase_a(PipeMaze(), testdata,  4)

testdata = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

# test cases
testcase_a(PipeMaze(), testdata,  4)

testdata = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

# test cases
testcase_a(PipeMaze(), testdata,  8)

testdata = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

# test cases
testcase_a(PipeMaze(), testdata,  8)

# 6856
testcase_a(PipeMaze(),   None, 6856)

# ========
#  Task B
# ========

# test cases
#testcase_b(C(), testdata,  2)

# 2
#testcase_b(C(),   None,    2)
