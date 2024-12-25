#!/usr/bin/env python3

__motd__ = "--- Day 13: Claw Contraption ---"

__url__ = "http://adventofcode.com/2024/day/13"

verbose = 0


class ClawMachine:
    """ """

    def __init__(self):
        pass

    def parseinput(self, input):
        """return list od machine dict"""
        input = input if type(input) == list else input.strip().splitlines()
        machines = []
        for line in input:
            if ":" in line:
                btn, xystr = line.split(":")
                xstr, ystr = xystr.split(",")
                if btn.startswith("Button A"):
                    adx, ady = int(xstr.split("+")[1]), int(ystr.split("+")[1])
                if btn.startswith("Button B"):
                    bdx, bdy = int(xstr.split("+")[1]), int(ystr.split("+")[1])
                if btn.startswith("Prize"):
                    px, py = int(xstr.split("=")[1]), int(ystr.split("=")[1])
                    machine = {
                        "adx": adx,
                        "ady": ady,
                        "bdx": bdx,
                        "bdy": bdy,
                        "px": px,
                        "py": py,
                    }
                    machines.append(machine)
        return machines

    def solver1(self, m):
        """calc (a,b) for single machine m to reach prize (px,py)"""
        # max times buttona can be pressed to reach prize
        maxa = min(1 + m["px"] // m["adx"], 1 + m["py"] // m["ady"])
        maxb = min(1 + m["px"] // m["bdx"], 1 + m["py"] // m["bdy"])
        for a in range(1, maxa):
            for b in range(1, maxb):
                # position after button A/B pressed a-times / b-times
                x = a * m["adx"] + b * m["bdx"]
                y = a * m["ady"] + b * m["bdy"]
                # prize reached !
                if x == m["px"] and y == m["py"]:
                    return a, b
        return None, None

    def downsolver1(self, m, offset=0):
        """calc (a,b) for single machine m to reach prize (px,py)"""
        # offset adjustment
        if offset > 0:
            offx = offset // m["bdx"] - 1
            offy = offset // m["bdy"] - 1
            m["px"] = m["px"] - (offset - m["bdx"] * offx)
            m["py"] = m["py"] - (offset - m["bdy"] * offy)
        # max times buttona can be pressed to reach prize
        maxa = min(m["px"] // m["adx"], m["py"] // m["ady"])
        maxb = min(m["px"] // m["bdx"], m["py"] // m["bdy"])
        i = 0
        for a in range(maxa, 1, -1):
            for b in range(maxb, 1, -1):
                i += 1
                # position after button A/B pressed a-times / b-times
                x = a * m["adx"] + b * m["bdx"]
                y = a * m["ady"] + b * m["bdy"]
                # prize reached !
                if verbose and x == m["px"] and y == m["py"]:
                    print(f'loop:{i} a:{a}, b:{b} calc x:{x}, y:{y} prize x:{m['px']} y:{m['py']}')
                    if offset == 0:
                        return a, b
                    return a + offx, b + offy
                # speedup
                if y < m["py"] or x < m["px"]:
                    break
        return None, None

    def solver(self, machines: list, offset=0) -> list:
        """solve machines list"""
        return [self.solver1(m) for m in machines]

    def downsolver(self, machines: list, offset=0) -> list:
        """solve machines list"""
        return [self.downsolver1(m, offset) for m in machines]

    def tokens(self, solutions) -> int:
        toks = [3 * a + 1 * b for a, b in solutions if a is not None and b is not None]
        return sum(toks)

    def task_a(self, input):
        """task A"""
        machines = self.parseinput(input)
        solutions = self.solver(machines)
        toks = self.tokens(solutions)
        return toks

    def task_b(self, input):
        """task B"""
        machines = self.parseinput(input)
        offset = 10000000000000
        solutions = self.downsolver(machines, offset)
        toks = self.tokens(solutions)
        return toks


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
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
# test cases
testcase(ClawMachine(), input, 480)

# 35729
testcase(ClawMachine(), None, 35729)

# ========
#  Task B
# ========

# test cases
testcase(ClawMachine(),  input,  941824595380, task_b=True)

#          224529 too low
#  99643084847415 too high
# 190447063630621
testcase(ClawMachine(), None, 0, task_b=True)
