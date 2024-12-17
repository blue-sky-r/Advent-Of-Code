#!/usr/bin/env python3

__motd__ = "--- Day 10: Hoof It ---"

__url__ = "http://adventofcode.com/2024/day/10"

verbose = 0


class Trailhead:

    def __init__(self):
        pass

    def parsemap(self, input):
        hmap = {}
        for y, line in enumerate(
            input if type(input) == list else input.strip().splitlines()
        ):
            for x, height in enumerate(line):
                hmap[(x, y)] = -1 if height == "." else int(height)
        return hmap, (x + 1, y + 1)

    def walk9(self, hmapdim, xy, visited):
        """walk to xy until peak 9 is reached"""
        hmap, dim = hmapdim
        # end reached ?
        if hmap[xy] == 9 and xy not in visited:
            return visited + [xy]
        # walk neigbours
        x, y = xy
        neighbors = [
            (nx, ny)
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if 0 <= nx < dim[0] and 0 <= ny < dim[1]
        ]
        # walk only +1 height
        eligible = [nxy for nxy in neighbors if hmap[nxy] - hmap[xy] == 1]
        for nxy in eligible:
            visited = self.walk9(hmapdim, nxy, visited)
        return visited

    def reach9(self, hmapdim):
        """find how many xy with height 9 can be rached"""
        hmap, dim = hmapdim
        # all starting xy with heaight 0
        start0xy = [xy for xy, h in hmap.items() if h == 0]
        reached = {}
        for xy in start0xy:
            found = self.walk9(hmapdim, xy, [])
            reached[xy] = found
        # startxy -> [(9xy), ...(9xy)]
        return reached

    def trail9(self, hmapdim, xy, trail):
        """get all trails to 9 from xy"""
        trail = trail + [xy]
        # print('entering:',xy,'trail:',trail)
        hmap, dim = hmapdim
        # end reached ?
        if hmap[xy] == 9:
            # print('reached 9:',xy)
            return trail
        # walk neigbours
        x, y = xy
        neighbors = [
            (nx, ny)
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if 0 <= nx < dim[0] and 0 <= ny < dim[1]
        ]
        # walk only +1 height
        eligible = [nxy for nxy in neighbors if hmap[nxy] - hmap[xy] == 1]
        newtrails = []
        for nxy in eligible:
            path = self.trail9(hmapdim, nxy, trail)
            if path:
                # print('adding path:',path)
                newtrails.append(path)
        # print('leaving xy:',xy,'newtrails:',newtrails)
        return newtrails

    def path9(self, hmapdim):
        """find the path to 9s"""
        hmap, dim = hmapdim
        # all starting xy with heaight 0
        start0xy = [xy for xy, h in hmap.items() if h == 0]
        paths = {}
        for xy in start0xy:
            path = self.trail9(hmapdim, xy, [])
            paths[xy] = path
        # startxy -> [(9xy), ...(9xy)]
        return paths

    def rating(self, trails: dict) -> int:
        """rating is the number of distinct hiking trails"""

        def listoflist(lol, flat) -> list:
            """flatten a list of lists"""
            if type(lol[0]) == tuple:
                flat.append(lol)
                return lol
            return [ listoflist(l, flat) for l in lol ]

        flat = []
        for xy, path in trails.items():
            l = listoflist(path, flat)
        return len(flat)

    def task_a(self, input):
        """task A"""
        hmapdim = self.parsemap(input)
        reached = self.reach9(hmapdim)
        return sum([len(reach) for xy, reach in reached.items()])

    def task_b(self, input):
        """task B"""
        hmapdim = self.parsemap(input)
        trails = self.path9(hmapdim)
        r = self.rating(trails)
        return r


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

# ========
#  Task B
# ========

input = """
.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
"""
# test cases
testcase(Trailhead(), input, 3, task_b=True)

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
testcase(Trailhead(), input, 13, task_b=True)

input = """
012345
123456
234567
345678
4.6789
56789.
"""
# test cases
testcase(Trailhead(), input, 227, task_b=True)

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
testcase(Trailhead(), input, 81, task_b=True)

# 1384
testcase(Trailhead(), None, 1384, task_b=True)
