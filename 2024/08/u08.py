#!/usr/bin/env python3

__motd__ = "--- Day 8: Resonant Collinearity ---"

__url__ = "http://adventofcode.com/2024/day/8"

import itertools

verbose = 0


class Antennas:

    def __init__(self):
        pass

    def printmap(self, mapdim, nodes=[], label=""):
        """for visual debugging only"""
        if not verbose:
            return
        map, dim = mapdim
        dimx, dimy = dim
        print()
        print(label)
        for y in range(dimy):
            for x in range(dimx):
                print("#" if (x, y) in nodes else map.get((x, y), "."), end="")
            print()
        print()

    def parsemap(self, input):
        map = {}
        for y, line in enumerate(input if type(input) == list else input.splitlines()[1:]):
            for x, sym in enumerate(line):
                if sym == ".":
                    continue
                xy = (x, y)
                map[xy] = sym
        return map, (x + 1, y + 1)

    def frequencies(self, mapdim) -> dict:
        """lookup freq -> [xy, xy2, ...]"""
        freq = {}
        for xy, f in mapdim[0].items():
            flst = freq.get(f, [])
            flst.append(xy)
            freq[f] = flst
        return freq

    def mirror(self, centerxy, xy, mapdim) -> tuple | None:
        """mirror xy around center xy"""
        # unpack
        map, dim = mapdim
        dimx, dimy = dim
        x, y = xy
        cx, cy = centerxy
        # calc mirror xy
        dx, dy = x - cx, y - cy
        mx, my = cx - dx, cy - dy
        # verift mx/my are on the map
        return (mx, my) if 0 <= mx < dimx and 0 <= my < dimy else None

    def antinodes(self, mapdim) -> list:
        nodes = []
        for freq, xylst in self.frequencies(mapdim).items():
            # need two antennas for antinode
            if len(xylst) == 1:
                continue
            # iterate combinarions
            for xy1, xy2 in itertools.combinations(xylst, 2):
                m1, m2 = self.mirror(xy1, xy2, mapdim), self.mirror(xy2, xy1, mapdim)
                if m1 and m1 not in nodes:
                    nodes.append(m1)
                if m2 and m2 not in nodes:
                    nodes.append(m2)
            self.printmap(mapdim, nodes, f"freq:{freq} @ xy:{xylst}")
        return nodes

    def mirror_harmonics(self, centerxy, xy, mapdim) -> list:
        """mirror xy around center xy with harminics"""
        # unpack
        map, dim = mapdim
        dimx, dimy = dim
        x, y = xy
        cx, cy = centerxy
        # calc harmonics ubtil out of the map
        dx, dy = x - cx, y - cy
        mx, my = cx, cy
        mxy = [centerxy]
        while True:
            # calc mirror xy
            mx, my = mx - dx, my - dy
            # verift mx/my are on the map
            if 0 <= mx < dimx and 0 <= my < dimy:
                mxy.append((mx, my))
            else:
                return mxy

    def antinodes_harmonics(self, mapdim) -> list:
        nodes = []
        for freq, xylst in self.frequencies(mapdim).items():
            # need two antennas for antinode
            if len(xylst) == 1:
                continue
            # iterate combinarions
            for xy1, xy2 in itertools.combinations(xylst, 2):
                for mxy in self.mirror_harmonics(xy1, xy2, mapdim) + self.mirror_harmonics(xy2, xy1, mapdim):
                    if mxy and mxy not in nodes:
                        nodes.append(mxy)
            self.printmap(mapdim, nodes, f"freq:{freq} @ xy:{xylst}")
        return nodes

    def task_a(self, input):
        """task A"""
        mapdim = self.parsemap(input)
        anodes = self.antinodes(mapdim)
        return len(anodes)

    def task_b(self, input):
        """task B"""
        mapdim = self.parsemap(input)
        anodes = self.antinodes_harmonics(mapdim)
        return len(anodes)


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
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
# test cases
testcase(Antennas(), input, 14)

# 367
testcase(Antennas(), None, 367)

# ========
#  Task B
# ========

# test cases
testcase(Antennas(), input, 34, task_b=True)

# 1285
testcase(Antennas(), None, 1285, task_b=True)
