#!/usr/bin/env python3

__motd__ = "--- Day 7: Bridge Repair ---"

__url__ = "http://adventofcode.com/2024/day/7"

verbose = 0


class CalibrationEquations:

    def parseeqs(self, input) -> list:
        """parse eqs to list, items are tuples (result, [terms])"""
        eqs = []
        for line in input if type(input) == list else input.splitlines():
            if not line:
                continue
            result, terms = line.split(": ")
            eq = (int(result), [int(i) for i in terms.split()])
            eqs.append(eq)
        return eqs

    def genresults(self, terms: list) -> int:
        """calc all equations, use bin mask as 0->+ 1->*"""
        gr = []
        # iterate all possible combinations
        for i in range(2 ** (len(terms) - 1)):
            calc = None
            # remove 0bxxx prefix
            oper = bin(i)[2:]
            # prefix 0 to get len(terms)-1 and create iterator
            operit = iter("0" * (len(terms) - 1 - len(oper)) + oper)
            for t in terms:
                if calc is None:
                    calc = t
                    continue
                op = next(operit)
                if op == "0":
                    calc = calc + t
                if op == "1":
                    calc = calc * t
            gr.append(calc)
            if verbose:
                print(f"i:{i} \t {oper:>8} \t calc={calc} \t {terms}")
        return gr

    def verifyeq(self, val, terms) -> bool:
        """try to solve eq left to right ignoring arth. precedence"""
        r = self.genresults(terms)
        return val in r

    def verifyeqs(self, eqs: list) -> list:
        """verify calib. eqs"""
        return [val for val, terms in eqs if self.verifyeq(val, terms)]

    def task_a(self, input):
        """task A"""
        eq = self.parseeqs(input)
        solved = self.verifyeqs(eq)
        return sum(solved)

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
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
# test cases
testcase(CalibrationEquations(), input, 3749)

# 7579994664753
testcase(CalibrationEquations(), None, 7579994664753)
