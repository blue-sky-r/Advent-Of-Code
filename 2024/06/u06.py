#!/usr/bin/env python3

__motd__ = "--- Day 6: Guard Gallivant ---"

__url__ = "http://adventofcode.com/2024/day/6"

verbose = 0


class GuardWalk:

    def printmap(self, mapdim, label: str = ""):
        """for visual debugging only"""
        if not verbose:
            return
        map, dim = mapdim
        dimx, dimy = dim
        print()
        print(label)
        for y in range(dimy):
            print("".join([map.get((x, y), ".") for x in range(dimx)]))
        print

    def rotate(self, dir: chr) -> chr:
        right90 = "^>v<"
        nxt = (right90.find(dir) + 1) % len(right90)
        return right90[nxt]

    def step(self, mapdim, xy) -> tuple:
        # expand tuples
        map, dim = mapdim
        dimx, dimy = dim
        x, y = xy
        # return if outside of the map dimensions
        if not (0 <= x < dimx and 0 <= y < dimy):
            return None
        dir = map[xy]
        # set xy as visited
        map[xy] = "X"
        # move in direction dir
        match dir:
            case "^":
                nxy = (x, y - 1)
            case "v":
                nxy = (x, y + 1)
            case ">":
                nxy = (x + 1, y)
            case "<":
                nxy = (x - 1, y)
        if map.get(nxy) == "#":
            ndir = self.rotate(dir)
            map[xy] = ndir
            return self.step(mapdim, xy)
        map[nxy] = dir
        return nxy

    def walk(self, mapdim):
        xy = [xy for xy in mapdim[0] if mapdim[0][xy] != "#"][0]
        while True:
            self.printmap(mapdim)
            xy = self.step(mapdim, xy)
            if not xy:
                break

    def parsemap(self, input):
        omap = {}
        input = input if type(input) == list else input.splitlines()[1:]
        for y, line in enumerate(input):
            for x, sym in enumerate(line):
                if sym != ".":
                    omap[(x, y)] = sym
        return omap, (x + 1, y + 1)

    def task_a(self, input):
        """task A"""
        obstacklemapdim = self.parsemap(input)
        self.walk(obstacklemapdim)
        visited = [xy for xy in obstacklemapdim[0] if obstacklemapdim[0][xy] == "X"]
        return len(visited)

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
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
# test cases
testcase(GuardWalk(), input, 41)

# 5131
testcase(GuardWalk(), None, 5131)
