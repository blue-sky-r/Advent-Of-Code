#!/usr/bin/env python3

__motd__ = "--- Day 7: Bridge Repair ---"

__url__ = "http://adventofcode.com/2024/day/7"

import itertools

verbose = 0


class CalibrationEquations:

    def __init__(self, op: str = "+*"):
        self.op = op

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

    def opgen(self, n):
        """Generate combinations of length n from operators"""
        return itertools.product(self.op, repeat=n)

    def opgen_(self, n):
        """Generate combinations of length n from operators (no itertools)"""
        def helper(current_combination, remaining_length):
            # Base case: if the remaining length is 0, yield the current combination
            if remaining_length == 0:
                yield tuple(current_combination)
            else:
                for op in self.op:
                    # Append the current element and recurse
                    current_combination.append(op)
                    yield from helper(current_combination, remaining_length - 1)
                    # Backtrack to explore other combinations
                    current_combination.pop()

        # Start the recursive helper function with an empty combination
        yield from helper([], n)

    def genresults(self, terms: list) -> int:
        """calc all equations, use bin mask as 0->+ 1->*"""
        gr = []
        # iterate all possible combinations of operators
        for optpl in self.opgen(len(terms) - 1):
            calc = None
            for j, t in enumerate(terms):
                if calc is None:
                    calc = t
                    continue
                op = optpl[j - 1]
                if op == "+":
                    calc = calc + t
                if op == "*":
                    calc = calc * t
                if op == "|":
                    calc = int("".join([str(calc), str(t)]))
            gr.append(calc)
            if verbose:
                print(f"{' '.join(optpl)} \t calc={calc} \t {terms}")
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
        eq = self.parseeqs(input)
        solved = self.verifyeqs(eq)
        return sum(solved)


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

# ========
#  Task B
# ========

# test cases
testcase(CalibrationEquations("+*|"), input, 11387, task_b=True)

# [53s] 438027111276610
testcase(CalibrationEquations("+*|"), None, 438027111276610, task_b=True)
