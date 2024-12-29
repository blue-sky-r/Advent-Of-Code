#!/usr/bin/env python3

__motd__ = "--- Day 14: Restroom Redoubt ---"

__url__ = "http://adventofcode.com/2024/day/14"

import re
from functools import reduce

verbose = 0


class Robots:

    def __init__(self, dim: tuple = (11, 7)):
        self.dim = dim

    def display(self, robots, label=""):
        if verbose == 0:
            return
        if label:
            print(label)
        dimx, dimy = self.dim
        for y in range(dimy):
            for x in range(dimx):
                robatxy = [r for r in robots if r["pos"] == (x, y)]
                if len(robatxy) == 0:
                    print(".", end="")
                else:
                    print(len(robatxy), end="")
            print()
        print()

    def parseinput(self, input):
        """p=0,4 v=3,-3"""
        input = input if type(input) == list else input.strip().splitlines()
        guards = []
        for line in input:
            if "," not in line:
                continue
            m = re.match(
                r"p=(?P<px>\d+),(?P<py>\d+) v=(?P<vx>-?\d+),(?P<vy>-?\d+)", line
            )
            g = {
                "pos": (int(m.group("px")), int(m.group("py"))),
                "v": (int(m.group("vx")), int(m.group("vy"))),
            }
            guards.append(g)
        return guards

    def moveguard(self, guard):
        xy = guard["pos"]
        newx = (xy[0] + guard["v"][0]) % self.dim[0]
        newy = (xy[1] + guard["v"][1]) % self.dim[1]
        guard["pos"] = (newx, newy)
        return guard

    def move(self, guards):
        """move guards"""
        return [self.moveguard(g) for g in guards]

    def movesec(self, guards, sec: int):
        """move gurads accoring to rules"""
        for t in range(sec):
            guards = self.move(guards)
            self.display(guards, f"time={t+1}")
        return guards

    def sectorscount(self, guards):
        """ """
        h2, v2 = self.dim[0] // 2, self.dim[1] // 2
        # separate guards to each sector
        sector0 = [g for g in guards if g["pos"][0] < h2 and g["pos"][1] < v2]
        sector1 = [g for g in guards if g["pos"][0] > h2 and g["pos"][1] < v2]
        sector2 = [g for g in guards if g["pos"][0] < h2 and g["pos"][1] > v2]
        sector3 = [g for g in guards if g["pos"][0] > h2 and g["pos"][1] > v2]
        return [len(sector0), len(sector1), len(sector2), len(sector3)]

    def calcsafetyfactor(self, guards):
        """calculate safety factor by multiplying number of robots in 4 sectors"""
        return reduce(lambda a, b: a * b, self.sectorscount(guards))

    def task_a(self, input):
        """task A"""
        guards = self.parseinput(input)
        self.display(guards, "Initial")
        guards = self.movesec(guards, 100)
        safety = self.calcsafetyfactor(guards)
        return safety

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
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
# test cases
testcase(Robots(), input, 12)

# 229069152
testcase(Robots(dim=(101,103)), None, 229069152)
