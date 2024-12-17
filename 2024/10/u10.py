#!/usr/bin/env python3

__motd__ = "--- Day 10: Hoof It ---"

__url__ = "http://adventofcode.com/2024/day/10"

import math

verbose = 0


class Trailhead:

    def __init__(self):
        pass

    def parsemap(self, input):
        hmap = {}
        for y, line in enumerate(input if type(input) == list else input.strip().splitlines()):
            for x, height in enumerate(line):
                hmap[(x, y)] = -1 if height == '.' else int(height)
        return hmap, (x+1, y+1)

    def walk(self, hmapdim, xy, visited):
        hmap, dim = hmapdim
        # end reached ?
        if hmap[xy] == 9 and xy not in visited:
            return visited + [xy]
        # walk
        x,y = xy
        neighbors = [(nx,ny) for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if 0<=nx<dim[0] and 0<=ny<dim[1]]
        eligible = [nxy for nxy in neighbors if hmap[nxy] - hmap[xy] == 1]
        for nxy in eligible:
            visited = self.walk(hmapdim, nxy, visited)
        return visited

    def reach9(self, hmapdim):
        hmap, dim = hmapdim
        # all starting xy
        start0xy = [xy for xy,h in hmap.items() if h == 0]
        reached = {}
        for xy in start0xy:
            found = self.walk(hmapdim, xy, [])
            reached[xy] = found
        return reached

    def task_a(self, input):
        """task A"""
        hmapdim = self.parsemap(input)
        reached = self.reach9(hmapdim)
        return sum([ len(reach) for xy,reach in reached.items()])

    def task_b(self, input):
        """task B"""
        return


def testcase(sut, input, result, task_b=False):
    """testcase verifies if input returns result"""
    # read default input file
    if input is None:
        data = __file__.replace(".py", ".input")
        with open(data) as f:
            input = [line.strip() for line in f]
    #
    print(f"TestCase {"B" if task_b else "A"} ", end="")
    print(f"for input: {data if 'data' in vars() else input}", end="")
    print(f"\t expected result: {result} ", end="")
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print(f"got: {r} \t {'[ OK ]' if r == result else '[ ERR ]'}")
    print()


# ========
#  Task A
# ========

input = """
0123
1234
8765
9876
"""
# test cases
testcase(Trailhead(), input, 1)

input = """
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
"""
# test cases
testcase(Trailhead(), input, 2)

input = """
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
"""
# test cases
testcase(Trailhead(), input, 4)

input = """
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
"""
# test cases
testcase(Trailhead(), input, 3)

input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
# test cases
testcase(Trailhead(), input, 36)

# 607
testcase(Trailhead(), None, 607)
